import re
from collections import defaultdict

with open('Day 4\\input') as file:
    lines = [line.rstrip() for line in file]

wins = defaultdict(lambda:1)
for line in lines:
    cards = re.split(':|\|', line)
    number = int(cards[0][5:])
    winning = set(cards[1].split())
    numbers = set(cards[2].split())
    hits = len(winning & numbers)
    wins[number] = wins[number] + 0

    for i in range(number + 1, number + 1 + hits):
        wins[i] = wins[i] + wins[number]

print(sum(wins.values()))