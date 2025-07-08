import json

from utils import get_resource_path


class ConfigLoader:
    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name
        self._full_path: str = get_resource_path(file_name)
        self._file = self._try_load_config()

    @property
    def get(self):
        if self._file is not None:
            return self._file
        else:
            print("Config doesn't exist")
            return None

    def save_config(self, new_data: dict) -> None:
        with open(self._full_path, "w", encoding="utf-8-sig") as f:
            json.dump(new_data, f, indent=4)

    def _try_load_config(self):
        try:
            with open(self._full_path, "r", encoding="utf-8-sig") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found {self._file_name}")
            return None
