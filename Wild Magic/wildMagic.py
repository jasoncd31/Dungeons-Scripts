# Created by Jason Douglas
# @jasoncd31 on GitHub

# Wild Magic Surge Table
# 1d100

# This takes in a json file and then chooses a random entry from it
import random
import json

# Open the json file
with open('Wild Magic/wildTable.json') as f:
    data = json.load(f)  # Load the json file into a variable


def wildMagic():
    # Choose a random entry from the json file
    choice = str(random.randint(1,len(data)))
    random_entry = data[choice]
    return random_entry

print(wildMagic())
