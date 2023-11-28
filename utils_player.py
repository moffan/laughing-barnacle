import csv


def get_player_stats(filename):
    player_stats = {}

    with open(filename) as file:
        reader = csv.reader(file, delimiter="|")
        for row in reader:
            if len(row) == 5:
                player_stats[row[1].strip()] = row[3].strip()
            elif len(row) == 4:
                player_stats[row[1].strip()] = row[2].strip()

    return player_stats
