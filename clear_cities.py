import json

with open('goroda.txt', encoding="utf-8") as f:
    goroda = f.readlines()


goroda = [g for g in goroda if len(g) > 1]

with open('goroda_rossii.txt', "w", encoding="utf-8") as o:
    o.writelines(goroda)
