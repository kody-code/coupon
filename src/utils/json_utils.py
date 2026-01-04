import json
from pathlib import Path


class JsonUtils:
    """Json工具类"""

    def __init__(self, json_file_path: Path):
        self.json_file_path = json_file_path

    def load(self) -> dict:
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        return json_data

    def ins(self, key: str, value: str):
        pass

    def get_price_and_discount(self):
        pass
