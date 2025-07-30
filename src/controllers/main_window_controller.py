import asyncio

from PySide6 import QtCore
from PySide6.QtCore import QObject, QDateTime, QDate
from PySide6.QtWidgets import QTableView

from models.daily_device_table import DailyDeviceTableModel
from models.deye_account import DeyeAccount
from models.electricity_price import ElectricityPrice
from models.monthly_device_table import MonthlyDeviceTableModel
from models.yearly_device_table import YearlyDeviceTableModel
from config_loader import ConfigLoader
from utils import ViewModes

from views.download_window_view import DownloadWindowView
from controllers.download_window_controller import DownloadWindowController


class MainWindowController(QObject):
    def __init__(self, deye_account: DeyeAccount, config: ConfigLoader, prices: ElectricityPrice, view_mode: ViewModes,
                 dialog_view: DownloadWindowView, dialog_controller: DownloadWindowController) -> None:
        super().__init__()

        self.__config = config
        self.__deye_account = deye_account
        self.__electricity_price = prices
        self.__current_view_mode = view_mode
        self.__current_table_model = None
        self.__dialog_view = dialog_view
        self.__dialog_controller = dialog_controller

        self.__is_startup = True
        self.__last_modified = ""

    @QtCore.Slot()
    def update_last_modify(self) -> None:
        if self.__is_startup:
            self.__deye_account.last_response_date = self.__config.get["lastUpdated"]
            self.__is_startup = False
        else:
            self.__last_modified: str = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm")
            self.__deye_account.last_response_date = self.__last_modified

    @QtCore.Slot()
    def on_insert_today_clicked(self) -> None:
        self.__deye_account.date = QDate.currentDate().toString("yyyy-MM-dd")

    @QtCore.Slot(QTableView)
    def on_get_data_clicked(self, table_view: QTableView) -> None:
        self.update_last_modify()

        asyncio.run(self.__get_data())

        table_view.setModel(self.__current_table_model)

    @QtCore.Slot(QDate)
    def on_date_edit_finished(self, date: QDate) -> None:
        self.__deye_account.date = date.toString("yyyy-MM-dd")

    @QtCore.Slot(str)
    def on_email_edit_finished(self, email: str) -> None:
        self.__deye_account.email = email

    @QtCore.Slot(str)
    def on_password_edit_finished(self, password: str) -> None:
        self.__deye_account.password = password

    @QtCore.Slot(str)
    def on_app_id_editing_finished(self, app_id: str) -> None:
        self.__deye_account.app_id = app_id

    @QtCore.Slot(str)
    def on_app_secret_editing_finished(self, app_secret: str) -> None:
        self.__deye_account.app_secret = app_secret

    @QtCore.Slot(ViewModes)
    def on_mode_view_toggled(self, view_mode: ViewModes) -> None:
        self.__current_view_mode = view_mode

    async def __get_data(self):
        self.__dialog_view.show()

        get_auth_token_task = asyncio.create_task(self.__deye_account.get_auth_token())
        get_device_list_task = asyncio.create_task(self.__deye_account.get_device_list(self.__current_view_mode))
        get_electricity_prices_task = asyncio.create_task(self.__electricity_price.get_prices(self.__deye_account.date))

        if not self.__deye_account.token_exist():
            self.__dialog_controller.update_status("Виконуємо вхід в акаунт...", 0)
            await get_auth_token_task

        self.__dialog_controller.update_status("Отримуємо список пристроїв...", 35)
        devices = await get_device_list_task
        total_consumption = [0.0 for _ in range(len(devices[0].consumption))]

        for device in devices:
            for i, consumption in enumerate(device.consumption):
                total_consumption[i] += consumption

        if self.__current_view_mode.value == ViewModes.DAY.value:
            self.__dialog_controller.update_status("Отримуємо ціни на електроенергію...", 70)
            prices = await get_electricity_prices_task
            self.__current_table_model = DailyDeviceTableModel(devices, total_consumption, prices)

        elif self.__current_view_mode.value == ViewModes.MONTH.value:
            self.__current_table_model = MonthlyDeviceTableModel(devices, total_consumption)

        elif self.__current_view_mode.value == ViewModes.YEAR.value:
            self.__current_table_model = YearlyDeviceTableModel(devices, total_consumption)

        self.__dialog_controller.update_status("Готово.", 100)

    def on_application_quit(self) -> None:
        if len(self.__last_modified) > 0:
            new_data = {
                "lastUpdated": self.__last_modified,
                "date": self.__deye_account.date,
                "email": self.__deye_account.email,
                "password": self.__deye_account.password,
                "appId": self.__deye_account.app_id,
                "appSecret": self.__deye_account.app_secret,
            }

            self.__electricity_price.quit()
            self.__config.save_config(new_data)

    def load_from_config(self) -> None:
        self.update_last_modify()

        self.__deye_account.email = self.__config.get["email"]
        self.__deye_account.password = self.__config.get["password"]
        self.__deye_account.app_id = self.__config.get["appId"]
        self.__deye_account.app_secret = self.__config.get["appSecret"]
        self.__deye_account.date = self.__config.get["date"]
