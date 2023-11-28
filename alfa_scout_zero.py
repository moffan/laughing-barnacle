import settings
import file_system
import utils_fm24_data
import utils_html
import utils_csv

print("### Welcome to fm scouting ###")

ranked_players = {}

files = file_system.get_html_files(settings.data_folder)
for f in files:
    filename = utils_fm24_data.convert_html_data_2_csv(f)
    players = utils_fm24_data.get_ranked_players_from_file(filename)
    utils_html.export_player_rankings(f.name, players)
    utils_csv.export_player_rankings(f.name, players)
