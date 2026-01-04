import os
import re
import shutil
from pathlib import Path

from src.config.constant import backup_path, home_path, json_parent_path
from src.utils.date_utils import get_tomorrow_date
from src.utils.excel_utils import ExcelUtils


class FileUtils:
    """文件工具类"""

    def create_file(self, file_name: str):
        """创建文件
        file_name: 文件名
        """
        json_path = self._get_json_file_list(json_parent_path)
        all_file_name = file_name + get_tomorrow_date() + ".xlsx"
        if len(json_path) > 0:
            excel_utils = ExcelUtils(
                json_path[0],
                Path(home_path / all_file_name),
            )
            excel_utils.json_to_excel()
            excel_utils.set_format()
        else:
            print("没有模板文件")

    def backup_file(self):
        """备份文件"""
        for file_path in self._get_excel_file_list(home_path):
            if not os.path.exists(file_path):
                continue
            file_name = self._get_file_name_from_path(file_path)
            date = self._get_date_from_file_name(file_name)
            os.makedirs(Path(backup_path / date), exist_ok=True)
            if os.path.exists(file_path):
                shutil.move(file_path, Path(backup_path / date / file_name))

    @staticmethod
    def _get_excel_file_list(file_path: str):
        """获取指定目录下的所有excel文件
        file_path: 文件路径
        """
        target_dir = Path(file_path)
        file_list = []
        for excel_file in target_dir.glob("*.xlsx"):
            file_list.append(str(excel_file))
        return file_list

    @staticmethod
    def _get_json_file_list(file_path: Path):
        """获取指定目录下的所有模板文件
        file_path: 文件路径
        """
        target_dir = Path(file_path)
        file_list = []
        for template_file in target_dir.glob("*.json"):
            file_list.append(str(template_file))
        return file_list

    @staticmethod
    def _get_file_name_from_path(file_path: str):
        """从文件路径中提取文件名
        file_path: 文件路径
        """
        return Path(file_path).name

    @staticmethod
    def _get_date_from_file_name(file_name: str):
        """从文件名提取 数字.数字 格式的日期/版本字符串
        file_name: 文件名
        """
        pattern = r"(\d+\.\d+)"
        match_result = re.search(pattern, file_name)
        return match_result.group(1) if match_result else ""
