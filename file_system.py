from os import path, makedirs, scandir
from json import load as _load_json
from pathlib import Path as _Path
from typing import List


def get_full_path(folder):
    p = _Path(folder)

    return p.resolve()


def create_folder_if_not_exist(folder):
    if not path.isdir(folder):
        makedirs(folder)


def get_all_files_in_folder(folder) -> List[str]:
    file_paths = []
    if path.isdir(folder):
        with scandir(folder) as entries:
            for entry in entries:
                if entry.is_file():
                    file_path = get_full_path(entry.path)
                    file_paths.append(file_path)

    return file_paths


def read_json_file(file_path):
    with open(file_path) as json_file:
        json_data = _load_json(json_file)

        return json_data
