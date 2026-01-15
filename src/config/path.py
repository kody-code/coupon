import os
from src.utils.workspace_utils import get_workspace_path, Path

workspace_path: Path = get_workspace_path()
home_path: Path = Path.home()

if os.getenv("MODE") == "dev":
    backup_path: Path = workspace_path / "backup"
    temp_path: Path = workspace_path / "temp"
else:
    backup_path: Path = home_path / "backup"
    temp_path: Path = home_path / "temp"