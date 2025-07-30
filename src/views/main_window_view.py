from PySide6.QtCore import QCoreApplication, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLineEdit

from controllers.main_window_controller import MainWindowController
from models.deye_account import DeyeAccount
from styles import Style
from ui.ui_MainWindow import Ui_MainWindow
from utils import convert_date, ViewModes


class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self, contr: MainWindowController, user: DeyeAccount, style: Style) -> None:
        super().__init__()

        self._controller: MainWindowController = contr
        self._user: DeyeAccount = user
        self.setupUi(self)

        QApplication.setStyle(QStyleFactory.create(style.value))
        QCoreApplication.instance().aboutToQuit.connect(self._controller.on_application_quit)

        self.fetchDataButton.clicked.connect(lambda: self._controller.on_get_data_clicked(self.tableView))
        self.dateEdit.userDateChanged.connect(self._controller.on_date_edit_finished)
        self.insertTodayDateButton.clicked.connect(self._controller.on_insert_today_clicked)
        self.emailLineEdit.textEdited.connect(self._controller.on_email_edit_finished)
        self.passwordLineEdit.textEdited.connect(self._controller.on_password_edit_finished)
        self.appIdLineEdit.textEdited.connect(self._controller.on_app_id_editing_finished)
        self.appSecretLineEdit.textEdited.connect(self._controller.on_app_secret_editing_finished)
        self.showPasswordButton.toggled.connect(
            lambda: self.show_password(self.passwordLineEdit, self.showPasswordButton.isChecked()))
        self.showAppSecretButton.toggled.connect(
            lambda: self.show_password(self.appSecretLineEdit, self.showAppSecretButton.isChecked()))
        self.dayRadioButton.toggled.connect(lambda: self._controller.on_mode_view_toggled(ViewModes.DAY))
        self.monthRadioButton.toggled.connect(lambda: self._controller.on_mode_view_toggled(ViewModes.MONTH))
        self.yearRadioButton.toggled.connect(lambda: self._controller.on_mode_view_toggled(ViewModes.YEAR))

        self._user.EmailChanged.connect(self.on_email_changed)
        self._user.PasswordChanged.connect(self.on_password_changed)
        self._user.AppIdChanged.connect(self.on_app_id_changed)
        self._user.AppSecretChanged.connect(self.on_app_secret_changed)
        self._user.DateChanged.connect(self.on_date_changed)
        self._user.LastResponseDateChanged.connect(self.on_last_response_date_changed)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, instance) -> None:
        if instance is not None:
            self._controller = instance

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
        self.dateEdit.setDate(convert_date(date))

    @Slot(QLineEdit, bool)
    def show_password(self, line_edit: QLineEdit, checked: bool) -> None:
        if checked:
            line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    @Slot(str)
    def on_last_response_date_changed(self, date: str) -> None:
        self.lastFetchedDateLabel.setText(date)
