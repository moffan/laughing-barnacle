import file_system


def get_data_folder_path():
    return file_system.get_full_path("data")


data_folder = get_data_folder_path()
file_system.create_folder_if_not_exist(data_folder)

output_folder = "./output"