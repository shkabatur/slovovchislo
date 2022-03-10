import json

with open('russian_names.json', encoding="utf-8") as f:
    d = json.load(f)
fnames = open("russian_names.txt", "w", encoding="utf-8")

for n in d:
    fnames.write(n["Name"].lower() + '\n')

f.close()

