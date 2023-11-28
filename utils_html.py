from bs4 import BeautifulSoup
import pandas as pd
import file_system
import settings


def export_player_rankings(filename, players):
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

    file_system.create_folder_if_not_exist(settings.output_folder)
    output_file = settings.output_folder + "/" + filename
    with open(output_file, "w+") as out_file:
        out_file.write(soup.prettify())
