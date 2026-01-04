from pathlib import Path


def get_project_root() -> Path:
    """
    获取项目根目录
    :return: 项目根目录
    """
    return Path(__file__).parent.parent.parent
