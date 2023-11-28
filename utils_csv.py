import file_system
import settings
import csv
import pandas as pd


def export_player_rankings(filename, players=None):
    file_system.create_folder_if_not_exist(settings.output_folder)
    out_filename = file_system.change_file_extension(filename, ".csv")
    output_path = settings.output_folder + "/rankings-" + out_filename

    df = pd.DataFrame(data=players)
    df_csv = df.to_csv()

    with open(output_path, "w+") as csv_file:
        # csv_writer = csv.writer(csv_file, delimiter=";")
        # csv_writer.writerows(df_csv)
        csv_file.write(df_csv)


def write_csv_data(filename, csv_data):
    with open(filename, "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerows(csv_data)
