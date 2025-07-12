from PySide6.QtCore import QObject, Signal


class ProgressModel(QObject):
    ProgressChanged = Signal(int)
    MessageChanged = Signal(str)

    def __init__(self):
        super().__init__()

        self._progress: int = 0
        self._message: str = ""

    @property
    def progress(self) -> int:
        return self._progress

    @progress.setter
    def progress(self, new_value: int) -> None:
        if 0 <= new_value <= 100:
            self._progress = new_value
            self.ProgressChanged.emit(self._progress)

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, new_message: str) -> None:
        self._message = new_message
        self.MessageChanged.emit(self._message)
