from PySide6.QtCore import QObject, Signal


class ProgressModel(QObject):
    ProgressChanged = Signal(int)
    MessageChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self.__progress = 0
        self.__message = ""

    @property
    def progress(self) -> int:
        return self.__progress

    @progress.setter
    def progress(self, new_value: int) -> None:
        if 0 <= new_value <= 100:
            self.__progress = new_value
            self.ProgressChanged.emit(self.__progress)

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, new_message: str) -> None:
        self.__message = new_message
        self.MessageChanged.emit(self.__message)
