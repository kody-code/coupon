from src.utils.folder_utils import get_folder_size, bytes_to_mb
from src.config.path import backup_path

def get_backup_folder_size():
    size = get_folder_size(str(backup_path))
    return bytes_to_mb(size)