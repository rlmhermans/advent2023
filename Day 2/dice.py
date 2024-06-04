import re
from functools import reduce
import operator

with open('input') as file:
    lines = [line.rstrip() for line in file]

sum = 0
for line in lines:
    colors = {'red': 0, 'green': 0, 'blue': 0}

    parsed_line = re.split(':|,|;', line[5:])
    for part in parsed_line[1:]:
        part = part.lstrip().split(' ')
        number, color = part
        number = int(number)

        if number > colors[color]: colors[color] = number

    sum += reduce(operator.mul, colors.values())

print(sum)