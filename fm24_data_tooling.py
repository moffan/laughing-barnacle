from bs4 import BeautifulSoup
from pathlib import PosixPath
import file_system
import csv
import roles
import calculations
from typing import Tuple


def _parse_data_row(data_row, data_tag="td"):
    data = []
    th = data_row.find_all(data_tag)
    for h in th:
        data.append(h.text)

    return data


def _convert_html_data_to_csv(html_content):
    csv_data = []
    soup = BeautifulSoup(html_content, "html.parser")
    for table in soup.find_all("table"):
        tr = table.find_all("tr")
        for index, row in enumerate(tr):
            data_row = _parse_data_row(row, "th" if index == 0 else "td")
            csv_data.append(data_row)
    return csv_data


def convert_html_data_2_csv(html_file: PosixPath):
    html_data = file_system.read_html_file(html_file)
    csv_data = _convert_html_data_to_csv(html_data)

    (name, folder) = file_system.get_file_info(html_file)
    filename = folder + "/" + name + ".csv"

    file_system.write_csv_data(filename, csv_data)

    return filename


def get_players_from_file(filename):
    players = []
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            players.append(row)

    return players


def rate_player(p) -> Tuple[str, str]:
    player_roles = roles.player_roles
    rankings = {}
    for ranked_role, value in player_roles.items():
        if not value:
            continue
        rankings[ranked_role] = calculations.calculate_weighted_average(p, value)

    return p["Name"], rankings


def get_ranked_players_from_file(filename: str):
    ranked_players = {}

    players = []
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            players.append(row)

    for p in players:
        (name, rankings) = rate_player(p)
        for r in rankings.items():
            (position, score) = r
            if position not in ranked_players:
                ranked_players[position] = {}
            ranked_players[position][name] = score

    return ranked_players
