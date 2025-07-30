import json
from typing import Any

from utils import get_resource_path


class ConfigLoader:
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name
        self.__full_path = get_resource_path(file_name)
        self.__file = self.__try_load_config()

    @property
    def get(self) -> Any:
        if self.__file is not None:
            return self.__file
        print("Config doesn't exist")
        return None

    def save_config(self, new_data: dict) -> None:
        with open(self.__full_path, "w", encoding="utf-8-sig") as f:
            json.dump(new_data, f, indent=4)

    def __try_load_config(self):
        try:
            with open(self.__full_path, "r", encoding="utf-8-sig") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found {self.__file_name}")
            return None
