import os
import sys

def get_folder_size(path: str) -> int:
    """
    递归计算文件夹总大小（单位：字节）
    :param path: 文件夹路径
    :return: 总大小（字节）
    """
    total_size = 0
    try:
        # 使用 os.scandir() 遍历目录，效率比 os.walk() 更高
        for entry in os.scandir(path):
            try:
                if entry.is_file(follow_symlinks=False):
                    total_size += entry.stat(follow_symlinks=False).st_size
                elif entry.is_dir(follow_symlinks=False):
                    total_size += get_folder_size(entry.path)
            except (PermissionError, FileNotFoundError):
                # 跳过无权限或已删除的文件
                continue
    except FileNotFoundError:
        print(f"错误：路径不存在 -> {path}")
        sys.exit(1)
    except NotADirectoryError:
        print(f"错误：提供的路径不是文件夹 -> {path}")
        sys.exit(1)
    return total_size

def bytes_to_mb(byte_size: int):
    """
    将字节数转换为 MB（保留两位小数）
    :param byte_size: int 或 float，字节数
    :return: float，MB 数值
    """
    
    return round(byte_size / (1024 * 1024), 2)