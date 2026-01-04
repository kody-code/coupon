import os
from pathlib import Path

from src.utils.path_utils import get_project_root

# 配置
if os.getenv("DEV_MODE") == "True":
    # 项目根目录
    home_path = Path(get_project_root() / "temp")
    # 缓存路径
    backup_path = Path(get_project_root() / "temp" / "backup")
    # Json路径
    json_parent_path = Path(get_project_root() / "data" / "json")
else:
    home = Path(os.path.expanduser("~"))
    # 桌面路径
    home_path = Path(home / "Desktop")
    # 备份路径
    backup_path = Path(home / "Desktop" / "backup")
    # Json路径
    json_parent_path = Path(home / "Desktop" / "json")
