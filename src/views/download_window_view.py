from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog
from models.progress import ProgressModel
from ui.ui_DownloadDialog import Ui_Dialog


class DownloadWindowView(QDialog, Ui_Dialog):
    def __init__(self, model: ProgressModel):
        super().__init__()
        self.setupUi(self)

        self.__model = model

        self.nextPushButton.setEnabled(False)
        self.nextPushButton.clicked.connect(self.close)

        self.cancelPushButton.setFocus()
        self.cancelPushButton.clicked.connect(self.close)

        self.__model.ProgressChanged.connect(self.__on_progress_changed)
        self.__model.MessageChanged.connect(self.__on_message_changed)

    @Slot(int)
    def __on_progress_changed(self, value: int) -> None:
        self.progressBar.setValue(value)
        if value == 100:
            self.nextPushButton.setEnabled(True)
            self.cancelPushButton.setEnabled(False)

    @Slot(str)
    def __on_message_changed(self, value: str) -> None:
        self.notificationLabel.setText(value)
