from pathlib import Path

def get_workspace_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent
    