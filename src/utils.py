import enum
import os
import sys
from typing import Final

from PySide6.QtCore import QDate

DATE_FORMAT: Final[str] = "yyyy-MM-dd"


def convert_date(date: str | QDate) -> QDate | str:
    if isinstance(date, QDate):
        return QDate.toString(date, DATE_FORMAT)
    else:
        return QDate.fromString(date, DATE_FORMAT)


class ViewModes(enum.Enum):
    DAY = "День"
    MONTH = "Місяць"
    YEAR = "Рік"


def get_resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.getcwd()

    return os.path.join(base_path, relative_path)
