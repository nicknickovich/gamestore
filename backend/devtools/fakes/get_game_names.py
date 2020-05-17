"""
Get names for top 100 PC games
from www.pcgamer.com

produce:
games.txt file with a list of game names
"""

import re
import requests
from bs4 import BeautifulSoup

base_url = "https://www.pcgamer.com/the-pc-gamer-top-100-now/"

game_list = []

for page_num in range(13):
    if page_num == 0:
        page_num = ""
    url = f"{base_url}{page_num}"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    s = soup.find_all("h2")

    for item in s:
        m = re.search(r"(\d\.)(.*)", item.contents[0])
        game_name = m.group(2).strip()
        game_list.append(game_name)

with open("games.txt", "w") as f:
    f.write("".join(f"{game}\n" for game in game_list))
