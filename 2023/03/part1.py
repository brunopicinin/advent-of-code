import re

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
lines = data.splitlines()

symbol_coords = set()
for x, line in enumerate(lines):
    for match in re.finditer(r"[^\d\.]", line):
        symbol_coords.add((x, match.start()))

matches = set()
for x, line in enumerate(lines):
    xmin = x - 1
    xmax = x + 2
    for match in re.finditer(r"\d+", line):
        ymin = match.start() - 1
        ymax = match.end() + 1
        for x_coord in range(xmin, xmax):
            for y_coord in range(ymin, ymax):
                if (x_coord, y_coord) in symbol_coords:
                    matches.add(match)

numbers = [int(match.group(0)) for match in matches]
print(sum(numbers))
