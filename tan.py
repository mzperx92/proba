adatok = []

with open("ufo_(small)_data.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok.append(sor.strip().split(","))

for i in adatok:
    print(i)