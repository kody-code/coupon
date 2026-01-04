from datetime import datetime, timedelta


def get_current_date(split: str = "."):
    """获取当前日期
    split: 分割符 默认为.
    """
    return datetime.now().strftime(f"%m{split}%d")


def get_tomorrow_date(split: str = "."):
    """获取明天的日期
    split: 分割符 默认为.
    """
    return (datetime.now() + timedelta(days=1)).strftime(f"%m{split}%d")
