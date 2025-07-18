﻿import sys

from PySide6.QtWidgets import QApplication

from controllers.main_window_controller import MainWindowController
from models.deye_account import DeyeAccount
from models.electricity_price import ElectricityPrice
from src.config_loader import ConfigLoader
from styles import Style
from utils import ViewModes
from views.download_window_view import DownloadWindowView
from controllers.download_window_controller import DownloadWindowController
from models.progress import ProgressModel
from views.main_window_view import MainWindowView


def main() -> None:
    app = QApplication(sys.argv)

    config = ConfigLoader("config.json")
    deye_account = DeyeAccount()
    electricity_price = ElectricityPrice()
    progress_model = ProgressModel()

    download_window_controller = DownloadWindowController(progress_model)
    download_window_view = DownloadWindowView(download_window_controller, progress_model)

    main_window_controller = MainWindowController(deye_account, config, electricity_price, ViewModes.DAY, download_window_view, download_window_controller)
    main_window_view = MainWindowView(main_window_controller, deye_account, Style.MACOS)

    main_window_view.show()

    main_window_controller.load_from_config()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
