import enum
import os
import sys


class ViewModes(enum.Enum):
    DAY = "День"
    MONTH = "Місяць"
    YEAR = "Рік"


def get_resource_path(relative_path: str) -> str:
    base_path = getattr(sys, "_MEIPASS", os.getcwd())
    return os.path.join(base_path, relative_path)
