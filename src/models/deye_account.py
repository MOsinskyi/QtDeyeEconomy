from datetime import datetime, timezone
from typing import Final

import requests
from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import QMessageBox

from models.device import Device
from src.models.user import User
from utils import ViewModes, DATE_FORMAT

BASE_URL: Final[str] = "https://eu1-developer.deyecloud.com/v1.0"

APP_ID_LENGTH: Final[int] = 15
APP_SECRET_LENGTH: Final[int] = 32


def get_daily_data(token: str, device_sn: str, date: str):
    url = f"{BASE_URL}/device/history"
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "bearer " + token
    }

    data = {
        "deviceSn": device_sn,
        "granularity": 1,
        "startAt": date,
        "endAt": date,
        "measurePoints": [
            "DailyActiveProduction",
            "DailyChargingEnergy",
            "DailyDischargingEnergy",
            "DailyEnergyBuy"
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        data_list = response.json().get("dataList", [])
        data_list.sort(key=lambda x: int(x.get("time", 0)))

        seen_hours: set[int] = set()
        generation: list[float] = []
        consumption: list[float] = []
        charge_energy: list[float] = []
        discharge_energy: list[float] = []

        for d in data_list:
            timestamp: int = int(d.get("time", 0))
            hour: int = datetime.fromtimestamp(timestamp, timezone.utc).hour

            if 1 <= hour <= 23 and hour not in seen_hours:
                seen_hours.add(hour)

                parse_daily_energy_stats(charge_energy, consumption, d, discharge_energy, generation)

        last = data_list[-1]

        parse_daily_energy_stats(charge_energy, consumption, last, discharge_energy, generation)

        while len(generation) < 24:
            generation.append(0.0)
            consumption.append(0.0)
            charge_energy.append(0.0)
            discharge_energy.append(0.0)

        return generation, consumption, charge_energy, discharge_energy

    except requests.exceptions.HTTPError as e:
        QMessageBox.critical(None, "Error", str(e))
        return None, None, None, None


def get_monthly_data(token: str, device_sn: str, date_end: str):
    date_start: str = datetime.strptime(date_end, "%Y-%m-%d").replace(day=1).strftime("%Y-%m-%d")

    url = f"{BASE_URL}/device/history"
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "bearer " + token
    }

    data = {
        "deviceSn": device_sn,
        "granularity": 2,
        "startAt": date_start,
        "endAt": date_end,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        data_list = response.json().get("dataList", [])

        generation: list[float] = []
        consumption: list[float] = []
        charge_energy: list[float] = []
        discharge_energy: list[float] = []

        for d in data_list:
            parse_monthly_energy_stats(charge_energy, discharge_energy, d, generation, consumption)

        while len(generation) < 31:
            generation.append(0.0)
            consumption.append(0.0)
            charge_energy.append(0.0)
            discharge_energy.append(0.0)

        return generation, consumption, charge_energy, discharge_energy

    except requests.exceptions.HTTPError as e:
        QMessageBox.critical(None, "Error", str(e))
        return None, None, None, None


def get_yearly_data(token: str, device_sn: str, date: str):
    year: str = str(QDate.fromString(date, DATE_FORMAT).year())
    date_start: str = f"{year}-01"
    date_end: str = f"{year}-12"

    url = f"{BASE_URL}/device/history"
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "bearer " + token
    }

    data = {
        "deviceSn": device_sn,
        "granularity": 3,
        "startAt": date_start,
        "endAt": date_end,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        data_list = response.json().get("dataList", [])

        generation: list[float] = []
        consumption: list[float] = []
        charge_energy: list[float] = []
        discharge_energy: list[float] = []

        is_passed: bool = False
        for d in data_list:
            month: int = QDate.fromString(d.get("time"), "yyyy-M").month()

            if month > 0 and not is_passed:
                for i in range(month):
                    generation.append(0.0)
                    consumption.append(0.0)
                    charge_energy.append(0.0)
                    discharge_energy.append(0.0)
                is_passed = True

            parse_monthly_energy_stats(charge_energy, discharge_energy, d, generation, consumption)

        while len(generation) < 12:
            generation.append(0.0)
            consumption.append(0.0)
            charge_energy.append(0.0)
            discharge_energy.append(0.0)

        return generation, consumption, charge_energy, discharge_energy

    except requests.exceptions.HTTPError as e:
        QMessageBox.critical(None, "Error", str(e))
        return None, None, None, None


def parse_daily_energy_stats(charge_energy: list[float], consumption: list[float], data, discharge_energy: list[float],
                             generation: list[float]) -> None:
    for item in data.get("itemList", []):
        key: str = item.get("key")
        value: float = float(item.get("value", 0))

        if key == "DailyActiveProduction":
            generation.append(value)
        elif key == "DailyEnergyBuy":
            consumption.append(value)
        elif key == "DailyChargingEnergy":
            charge_energy.append(value)
        elif key == "DailyDischargingEnergy":
            discharge_energy.append(value)


def parse_monthly_energy_stats(charge_energy: list[float], discharge_energy: list[float], data,
                               generation: list[float], consumption: list[float]) -> None:
    for item in data.get("itemList", []):
        key: str = item.get("key")
        value: float = float(item.get("value", 0))

        if key == "Production":
            generation.append(value)
        elif key == "Consumption":
            consumption.append(value)
        elif key == "ChargingCapacity":
            charge_energy.append(value)
        elif key == "DischargingCapacity":
            discharge_energy.append(value)


class DeyeAccount(User):
    AppIdChanged = Signal(str)
    AppSecretChanged = Signal(str)
    DateChanged = Signal(str)
    LastResponseDateChanged = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._app_id: str = ""
        self._app_secret: str = ""
        self._date: str = ""
        self._last_response_date: str = ""
        self._token: str = ""

    @property
    def app_id(self) -> str:
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: str) -> None:
        if len(app_id) == APP_ID_LENGTH:
            self._app_id = app_id
            self.AppIdChanged.emit(app_id)

    @property
    def app_secret(self) -> str:
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret: str) -> None:
        if len(app_secret) == APP_SECRET_LENGTH:
            self._app_secret = app_secret
            self.AppSecretChanged.emit(app_secret)

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date: str) -> None:
        self._date = date
        self.DateChanged.emit(date)

    @property
    def last_response_date(self) -> str:
        return self._last_response_date

    @last_response_date.setter
    def last_response_date(self, date: str) -> None:
        self._last_response_date = date
        self.LastResponseDateChanged.emit(date)

    def token_exist(self) -> bool:
        return self._token != ""

    async def get_auth_token(self) -> str:
        url = f'{BASE_URL}/account/token?appId={self._app_id}'
        headers = {'Content-Type': 'application/json'}

        data = {
            "appSecret": self._app_secret,
            "email": self.email,
            "password": self.password_hash
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            self._token = response.json()["accessToken"]
        except requests.exceptions.ConnectionError:
            QMessageBox.critical(None, "Помилка", "Перевірте інтернет з'єднання!")
        except KeyError:
            QMessageBox.critical(None, "Помилка", "Перевірте правильність введених даних!")

        return self._token

    async def get_device_list(self, view_mode: ViewModes) -> list[Device]:
        url = f"{BASE_URL}/station/listWithDevice"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'bearer ' + self._token
        }
        data = {
            "deviceType": "INVERTER",
            "page": 1,
            "size": 10
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        devices: list[Device] = []

        for station in response.json().get("stationList", []):
            for device in station.get("deviceListItems", []):
                sn: str = device.get("deviceSn")
                if view_mode.value == ViewModes.DAY.value:
                    generation, consumption, charge, discharge = get_daily_data(self._token, sn, self._date)
                    devices.append(Device(sn, generation, consumption, charge, discharge))
                elif view_mode.value == ViewModes.MONTH.value:
                    generation, consumption, charge, discharge = get_monthly_data(self._token, sn, self._date)
                    devices.append(Device(sn, generation, consumption, charge, discharge))
                elif view_mode.value == ViewModes.YEAR.value:
                    generation, consumption, charge, discharge = get_yearly_data(self._token, sn, self._date)
                    devices.append(Device(sn, generation, consumption, charge, discharge))

        return devices
