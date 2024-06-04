import re
from collections import defaultdict
from functools import reduce
import operator

with open('Day 3\input') as file:
    lines = [line.rstrip() for line in file]

r = re.compile(r'\d+')

def get_gear_neighbour(m, x, y):
    rows, cols = range(len(m)),range(len(m[0]))
    offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    result = 0
    for dy,dx in offsets:
        ny, nx = y + dy, x + dx
        if ny in rows and nx in cols and m[ny][nx] == '*':
            result = (ny, nx)
    return result

sum = 0
gears = defaultdict(set)
for idx, line in enumerate(lines):
    digits = [(x.span(), x.group()) for x in r.finditer(line)]
    for span, digit in digits:
        for i in range(span[0], span[1]):
            gear_neighbour = get_gear_neighbour(lines, i, idx)
            if gear_neighbour: gears[gear_neighbour].add(int(digit))

for k, v in gears.items():
    if len(v) > 1:
        sum += reduce(operator.mul, v)

print(sum)