import os

from src.utils import get_resource_path


def test_get_resource_path() -> None:
    expected_path = os.path.abspath("config.json")
    assert get_resource_path("config.json") == expected_path
