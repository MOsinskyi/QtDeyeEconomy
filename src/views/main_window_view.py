from PySide6.QtCore import QCoreApplication, Slot, QDate
from PySide6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLineEdit

from controllers.main_window_controller import MainWindowController
from models.deye_account import DeyeAccount
from styles import Style
from ui.ui_MainWindow import Ui_MainWindow
from utils import ViewModes


class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self, controller: MainWindowController, user: DeyeAccount, style: Style) -> None:
        super().__init__()

        self.__controller = controller
        self.__user = user
        self.__app_instance = QCoreApplication.instance()
        self.setupUi(self)

        QApplication.setStyle(QStyleFactory.create(style.value))

        if self.__app_instance is not None:
            self.__app_instance.aboutToQuit.connect(self.__controller.on_application_quit)

        self.fetchDataButton.clicked.connect(lambda: self.__controller.on_get_data_clicked(self.tableView))
        self.dateEdit.userDateChanged.connect(self.__controller.on_date_edit_finished)
        self.insertTodayDateButton.clicked.connect(self.__controller.on_insert_today_clicked)
        self.emailLineEdit.textEdited.connect(self.__controller.on_email_edit_finished)
        self.passwordLineEdit.textEdited.connect(self.__controller.on_password_edit_finished)
        self.appIdLineEdit.textEdited.connect(self.__controller.on_app_id_editing_finished)
        self.appSecretLineEdit.textEdited.connect(self.__controller.on_app_secret_editing_finished)
        self.showPasswordButton.toggled.connect(lambda: self.show_password(self.passwordLineEdit,
                                                                           self.showPasswordButton.isChecked()))
        self.showAppSecretButton.toggled.connect(lambda: self.show_password(self.appSecretLineEdit,
                                                                            self.showAppSecretButton.isChecked()))
        self.dayRadioButton.toggled.connect(lambda: self.__controller.on_mode_view_toggled(ViewModes.DAY))
        self.monthRadioButton.toggled.connect(lambda: self.__controller.on_mode_view_toggled(ViewModes.MONTH))
        self.yearRadioButton.toggled.connect(lambda: self.__controller.on_mode_view_toggled(ViewModes.YEAR))

        self.__user.EmailChanged.connect(self.on_email_changed)
        self.__user.PasswordChanged.connect(self.on_password_changed)
        self.__user.AppIdChanged.connect(self.on_app_id_changed)
        self.__user.AppSecretChanged.connect(self.on_app_secret_changed)
        self.__user.DateChanged.connect(self.on_date_changed)
        self.__user.LastResponseDateChanged.connect(self.on_last_response_date_changed)

    @property
    def controller(self) -> MainWindowController:
        return self.__controller

    @controller.setter
    def controller(self, instance: MainWindowController) -> None:
        if instance is not None:
            self.__controller = instance

    @Slot(str)
    def on_email_changed(self, email: str) -> None:
        self.emailLineEdit.setText(email)

    @Slot(str)
    def on_password_changed(self, password: str) -> None:
        self.passwordLineEdit.setText(password)

    @Slot(str)
    def on_app_id_changed(self, app_id: str) -> None:
        self.appIdLineEdit.setText(app_id)

    @Slot(str)
    def on_app_secret_changed(self, app_secret: str) -> None:
        self.appSecretLineEdit.setText(app_secret)

    @Slot(str)
    def on_date_changed(self, date: str) -> None:
        self.dateEdit.setDate(QDate.fromString(date, "yyyy-MM-dd"))

    @Slot(QLineEdit, bool)
    def show_password(self, line_edit: QLineEdit, checked: bool) -> None:
        if checked:
            line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    @Slot(str)
    def on_last_response_date_changed(self, date: str) -> None:
        self.lastFetchedDateLabel.setText(date)
