import csv


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
