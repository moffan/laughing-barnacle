from pathlib import Path as _Path


def get_data_folder_path():
    p = _Path("data")

    return p.resolve()
