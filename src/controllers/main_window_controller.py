from PySide6 import QtCore
from PySide6.QtCore import QObject, QDateTime, QAbstractTableModel
from PySide6.QtWidgets import QTableView

from models.device import Device
from models.daily_device_table import DailyDeviceTableModel
from models.deye_account import DeyeAccount
from models.electricity_price import ElectricityPrice
from models.monthly_device_table import MonthlyDeviceTableModel
from models.yearly_device_table import YearlyDeviceTableModel
from src.config_loader import ConfigLoader
from src.utils import *


class MainWindowController(QObject):
    def __init__(self, deye_account: DeyeAccount, config: ConfigLoader, prices: ElectricityPrice,
                 view_mode: ViewModes) -> None:
        super().__init__()

        self._config = config
        self._deye_account = deye_account
        self._electricity_price: ElectricityPrice = prices
        self._current_view_mode: ViewModes = view_mode
        self._current_table_model: QAbstractTableModel = None

        self._is_startup: bool = True
        self._last_modified: str = ""

    @QtCore.Slot()
    def update_last_modify(self) -> None:
        if self._is_startup:
            self._deye_account.last_response_date = self._config.get["lastUpdated"]
            self._is_startup = False
        else:
            self._last_modified: str = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm")
            self._deye_account.last_response_date = self._last_modified

    @QtCore.Slot()
    def on_insert_today_clicked(self) -> None:
        self._deye_account.date = convert_date(QDate.currentDate())

    @QtCore.Slot(QTableView)
    def on_get_data_clicked(self, table_view: QTableView) -> None:
        self.update_last_modify()

        self._deye_account.get_auth_token()
        devices: list[Device] = self._deye_account.get_device_list(self._current_view_mode)
        total_consumption: list[float] = [0.0 for _ in range(len(devices[0].consumption))]

        for device in devices:
            for i in range(len(device.consumption)):
                total_consumption[i] += device.consumption[i]

        if self._current_view_mode.value == ViewModes.DAY.value:
            prices: list[float] = self._electricity_price.get_prices(self._deye_account.date)
            self._current_table_model = DailyDeviceTableModel(devices, total_consumption, prices)

        elif self._current_view_mode.value == ViewModes.MONTH.value:
            self._current_table_model = MonthlyDeviceTableModel(devices, total_consumption)

        elif self._current_view_mode.value == ViewModes.YEAR.value:
            self._current_table_model = YearlyDeviceTableModel(devices, total_consumption)

        table_view.setModel(self._current_table_model)

    @QtCore.Slot(QDate)
    def on_date_edit_finished(self, date: QDate) -> None:
        self._deye_account.date = convert_date(date)

    @QtCore.Slot(str)
    def on_email_edit_finished(self, email: str) -> None:
        self._deye_account.email = email

    @QtCore.Slot(str)
    def on_password_edit_finished(self, password: str) -> None:
        self._deye_account.password = password

    @QtCore.Slot(str)
    def on_app_id_editing_finished(self, app_id: str) -> None:
        self._deye_account.app_id = app_id

    @QtCore.Slot(str)
    def on_app_secret_editing_finished(self, app_secret: str) -> None:
        self._deye_account.app_secret = app_secret

    @QtCore.Slot(ViewModes)
    def on_mode_view_toggled(self, view_mode: ViewModes) -> None:
        self._current_view_mode = view_mode

    def on_application_quit(self) -> None:
        if len(self._last_modified) > 0:
            new_data: dict = {
                "lastUpdated": self._last_modified,
                "date": self._deye_account.date,
                "email": self._deye_account.email,
                "password": self._deye_account.password,
                "appId": self._deye_account.app_id,
                "appSecret": self._deye_account.app_secret,
            }

            self._electricity_price.quit()
            self._config.save_config(new_data)


    def load_from_config(self) -> None:
        self.update_last_modify()

        self._deye_account.email = self._config.get["email"]
        self._deye_account.password = self._config.get["password"]
        self._deye_account.app_id = self._config.get["appId"]
        self._deye_account.app_secret = self._config.get["appSecret"]
        self._deye_account.date = self._config.get["date"]

