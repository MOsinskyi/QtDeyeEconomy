from PySide6.QtCore import QObject

from models.progress import ProgressModel


class DownloadWindowController(QObject):
    def __init__(self, model: ProgressModel) -> None:
        super().__init__()

        self._model: ProgressModel = model

    def update_status(self, message: str, progress: int):
        self._model.progress = progress
        self._model.message = message

    def clear_status(self) -> None:
        self._model.progress = 0
        self._model.message = ""
