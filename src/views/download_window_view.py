﻿from PySide6 import QtCore
from PySide6.QtWidgets import QDialog

from controllers.download_window_controller import DownloadWindowController
from models.progress import ProgressModel
from ui.ui_DownloadDialog import Ui_Dialog


class DownloadWindowView(QDialog, Ui_Dialog):
    def __init__(self, controller: DownloadWindowController, model: ProgressModel):
        super().__init__()
        self.setupUi(self)

        self._controller: DownloadWindowController = controller
        self._model: ProgressModel = model

        self.nextPushButton.setEnabled(False)
        self.nextPushButton.clicked.connect(self.close)

        self.cancelPushButton.setFocus()
        self.cancelPushButton.clicked.connect(self.close)

        self._model.ProgressChanged.connect(self._on_progress_changed)
        self._model.MessageChanged.connect(self._on_message_changed)

    @QtCore.Slot(int)
    def _on_progress_changed(self, value: int) -> None:
        self.progressBar.setValue(value)
        if value == 100:
            self.nextPushButton.setEnabled(True)
            self.cancelPushButton.setEnabled(False)

    @QtCore.Slot(str)
    def _on_message_changed(self, value: str) -> None:
        self.notificationLabel.setText(value)

