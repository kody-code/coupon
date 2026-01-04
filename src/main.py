import inquirer
from dotenv import load_dotenv

from src.utils.path_utils import get_project_root

load_dotenv(get_project_root() / ".env")
from src.config.constant import json_parent_path
from src.utils.file_utils import FileUtils
from src.utils.json_utils import JsonUtils

# 所有文件名称
file_names: list = [
    "京东优惠券",
    "淘宝优惠券",
    "活动班",
]


def choose_file():
    """选择文件, 默认为 京东优惠券

    通过交互式命令行界面让用户选择要创建的文件，
    支持单个文件创建或批量创建所有文件
    """
    questions = [
        inquirer.List(
            "file",
            message="请选择文件",
            choices=[
                "全部",
            ]
            + file_names,
            default="京东优惠券",
            carousel=True,
        ),
    ]

    answers = inquirer.prompt(questions)
    if answers:
        if answers["file"] == "全部":
            for file_name in file_names:
                try:
                    FileUtils().create_file(file_name)
                    print("创建文件：" + file_name)
                except Exception as e:
                    print(f"创建文件 {file_name} 失败: {e}")
        else:
            try:
                FileUtils().create_file(answers["file"])
                print("创建文件：" + answers["file"])
            except Exception as e:
                print(f"创建文件失败: {e}")


def action():
    """选择操作

    提供两种操作选项：
    1. 备份并创建文件 - 先备份现有文件，再执行文件创建
    2. 创建文件 - 直接创建文件
    """
    questions = [
        inquirer.List(
            "action",
            message="请选择操作",
            choices=["备份并创建文件", "创建文件"],
            default="备份并创建文件",
            carousel=True,
        ),
    ]

    answers = inquirer.prompt(questions)

    if answers:
        if answers["action"] == "备份并创建文件":
            try:
                FileUtils().backup_file()
                choose_file()
            except Exception as e:
                print(f"备份文件时出错: {e}")
        elif answers["action"] == "创建文件":
            choose_file()


def main():
    """程序主入口

    执行用户选择的操作
    """
    action()


if __name__ == "__main__":
    data = JsonUtils(json_parent_path / "优惠券.json").load()

    for item in data:
        for index, value in enumerate(data[item]):
            value["PC"] = index + 1
            print(value)
