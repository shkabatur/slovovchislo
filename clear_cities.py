import json

with open('cities.json', encoding="utf-8") as f:
    d = json.load(f)
cities = open("cities.txt", "w", encoding="utf-8")

for c in d["city"]:
    cities.write(c["name"].lower() + '\n')

cities.close()

