import os
from pathlib import Path
from src.config.path import temp_path, backup_path
from src.utils.data_utils import get_backup_folder_size

def init_dir():
    if not Path(temp_path).is_dir():
        os.makedirs(temp_path, True)
    if not Path(backup_path).is_dir():
        os.makedirs(backup_path, True)
        

if __name__ == '__main__':
    # init_dir()
    print(get_backup_folder_size())