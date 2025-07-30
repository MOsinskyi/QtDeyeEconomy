import hashlib

from PySide6.QtCore import Signal, QObject


class User(QObject):
    EmailChanged = Signal(str)
    PasswordChanged = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.__email = ""
        self.__password = ""

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    @property
    def password_hash(self) -> str:
        return hashlib.sha256(self.__password.encode("utf-8")).hexdigest()

    @password.setter
    def password(self, password: str) -> None:
        if len(password) > 0:
            self.__password = password
            self.PasswordChanged.emit(password)

    @email.setter
    def email(self, email: str) -> None:
        if len(email) > 0:
            self.__email = email
            self.EmailChanged.emit(email)
