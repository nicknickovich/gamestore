"""
Create a list of users in json format

produce:
users.json file
"""

import json
import random
import uuid

from faker import Faker


fake = Faker()

N_USERS = 100
default_avatar = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

users = []
for _ in range(N_USERS):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name}_{last_name}"
    new_user = {
        "uuid": str(uuid.uuid4()),
        "email": fake.email(),
        "avatar": default_avatar,
        "account_created": fake.iso8601(),
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": fake.password(),
    }
    users.append(new_user)

with open("users.json", "w") as f:
    json.dump(users, f, indent=2, separators=(",", ": "))
