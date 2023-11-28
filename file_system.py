import os
from json import load as _load_json
from pathlib import PosixPath, Path
from typing import List, Tuple


def change_file_extension(filename, file_extension):
    split_tup = os.path.splitext(filename)
    
    return split_tup[0] + file_extension


def get_full_path(folder):
    p = Path(folder)

    return p.resolve()


def get_file_info(f: PosixPath) -> Tuple[str, str]:
    path_info = Path(f)

    return path_info.stem, str(f.parent)


def create_folder_if_not_exist(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)


def get_all_files_in_folder(folder, file_extension=None) -> List[str]:
    file_paths = []
    if os.path.isdir(folder):
        with os.scandir(folder) as entries:
            for entry in entries:
                if entry.is_file():
                    if file_extension and not entry.path.endswith(file_extension):
                        continue
                    file_path = get_full_path(entry.path)
                    file_paths.append(file_path)

    return file_paths


def read_json_file(file_path):
    with open(file_path) as json_file:
        json_data = _load_json(json_file)

        return json_data


def get_html_files(data_folder) -> List[PosixPath]:
    _file_extension = ".html"
    html_files = get_all_files_in_folder(data_folder, _file_extension)

    return html_files


def read_html_file(file_path):
    with open(file_path) as html_file:
        content = html_file.read()

        return content


