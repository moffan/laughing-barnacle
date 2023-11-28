from bs4 import BeautifulSoup
import pandas as pd
import file_system


def _parse_data_row(data_row, data_tag="td"):
    data = []
    th = data_row.find_all(data_tag)
    for h in th:
        data.append(h.text)

    return data


def export_ranked_players(filename, players):
    default_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>ranked players</title>
    </head>
    <body></body>
    </html>
    """

    soup = BeautifulSoup(default_html, "html.parser")

    df = pd.DataFrame(data=players)
    df_html = df.to_html()
    soup.body.append(BeautifulSoup(df_html, "html.parser"))

    output_folder = "./output"
    file_system.create_folder_if_not_exist(output_folder)
    output_file = output_folder + "/report-" + filename
    with open(output_file, "w+") as out_file:
        out_file.write(soup.prettify())
