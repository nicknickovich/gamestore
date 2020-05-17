"""
Create a list of games in json format

require:
games.txt file with a list of game names in the same directory

produce:
games.json file
"""

import json
import random
import uuid


with open("games.txt") as f:
    game_names = f.read().splitlines()

default_cover = "https://cdn.pixabay.com/photo/2016/03/31/18/02/controller-1294077_960_720.png"
default_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel ante rutrum, dapibus ligula sed, congue justo. Aliquam odio libero, porta ac dapibus lobortis, eleifend a justo. Morbi ac turpis in est volutpat suscipit. Nullam sagittis dolor at imperdiet tincidunt. Nulla posuere pharetra enim. Maecenas a imperdiet lorem. Maecenas id ligula sodales, tempus dui vel, consequat risus. Sed a pharetra sem, nec feugiat arcu. Quisque porttitor sodales neque eget varius. Phasellus eget ornare odio, sit amet tempor lacus. Suspendisse vitae mauris at lacus cursus lobortis. "

games = []
for name in game_names:
    new_game = {
        "name": name,
        "price": round(random.uniform(2.5, 20), 2),
        "cover_image": default_cover,
        "description": default_description,
        "uuid": str(uuid.uuid4())
    }
    games.append(new_game)

with open("games.json", "w") as f:
    json.dump(games, f, indent=2, separators=(",", ": "))
