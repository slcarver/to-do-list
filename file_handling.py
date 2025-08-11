import json

try:
    with open ("to-do.json", mode="r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = {}


with open ("to-do.json", mode="w", encoding="utf-8") as write_file:
    json.dump(existing_data, write_file, indent=4)

    