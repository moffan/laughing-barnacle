import os

from watchfiles import watch

import base_weights
import calculations
import player_tooling
import config


data_folder = config.get_data_folder_path()

# def setup():
if not os.path.isdir(data_folder):
    os.makedirs(data_folder)

for changes in watch(data_folder):
    change = changes.pop()
    (_, file_path) = change
    filename = os.path.splitext(os.path.basename(file_path))[0]

    cutoff = 0
    stats = player_tooling.get_player_stats(file_path)

    rankings = {
        "cd": calculations.calculate_ratings(stats, base_weights.cd, cutoff),
        "fb": calculations.calculate_ratings(stats, base_weights.fb, cutoff),
        "dm": calculations.calculate_ratings(stats, base_weights.dm, cutoff),
        "w": calculations.calculate_ratings(stats, base_weights.w, cutoff),
        "am": calculations.calculate_ratings(stats, base_weights.am, cutoff),
        "st": calculations.calculate_ratings(stats, base_weights.st, cutoff),
    }

    print(filename + " : " + str(rankings))
