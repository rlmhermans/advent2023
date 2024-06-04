import re

with open('input') as file:
    lines = [line.rstrip() for line in file]

word_calibrations = {
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9', 
    'zero': '0'
    }

sum = 0
for line in lines:
    digits = re.findall('(?=(0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine))', line)
    f = word_calibrations.get(digits[0], digits[0])
    l = word_calibrations.get(digits[-1], digits[-1])
    sum += int(f+l)
        
print(sum)
