import os

from watchfiles import watch

import base_weights
import calculations
import player_tooling
import config

from file_system import (
    create_folder_if_not_exist,
    get_all_files_in_folder,
    read_json_file,
)

print("### Welcome to fm scouting ###")

data_folder = config.get_data_folder_path()
create_folder_if_not_exist(data_folder)

known_roles = get_all_files_in_folder("settings")

if not known_roles:
    roles = base_weights.weights
else:
    roles = {}
    for role in known_roles:
        roles[role.stem] = read_json_file(role)

for changes in watch(data_folder):
    change = changes.pop()
    (_, file_path) = change
    filename = os.path.splitext(os.path.basename(file_path))[0]

    cutoff = 0
    stats = player_tooling.get_player_stats(file_path)

    rankings = {}
    for ranked_role, value in roles.items():
        if not value:
            continue

        rankings[ranked_role] = calculations.calculate_weighted_average(stats, value)

    print(filename + " : " + str(rankings))
