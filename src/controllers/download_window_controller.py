from PySide6.QtCore import QObject
from models.progress import ProgressModel


class DownloadWindowController(QObject):
    def __init__(self, model: ProgressModel) -> None:
        super().__init__()
        self.__model = model

    def update_status(self, message: str, progress: int) -> None:
        self.__model.progress = progress
        self.__model.message = message

    def clear_status(self) -> None:
        self.__model.progress = 0
        self.__model.message = ""
