from watchfiles import watch
import calculations
import csv
import os
import player_tooling

from settings import data_folder
from roles import player_roles


def get_temp_player_data(filename):
    player_attributes = []

    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter="|")
        for row in spamreader:
            if len(row) > 4:
                player_attributes.append(row)

    return player_attributes


def create_attribute_file(filename):
    player_attributes = get_temp_player_data(filename)
    with open("attributes.txt", "w") as fp:
        for item in player_attributes:
            if "-" not in item:
                value = item[1].strip()
                fp.write("'%s':'',\n" % value)
    print("Done")


def watch_players():
    for changes in watch(data_folder):
        change = changes.pop()
        (_, file_path) = change
        filename = os.path.splitext(os.path.basename(file_path))[0]

        stats = player_tooling.get_player_stats(file_path)

        rankings = {}
        for ranked_role, value in player_roles.items():
            if not value:
                continue

            rankings[ranked_role] = calculations.calculate_weighted_average(
                stats, value
            )

        print(filename + " : " + str(rankings))
