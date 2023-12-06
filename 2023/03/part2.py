import re
from collections import defaultdict

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
lines = data.splitlines()

symbol_coords = set()
for x, line in enumerate(lines):
    for match in re.finditer(r"\*", line):
        symbol_coords.add((x, match.start()))

matches = defaultdict(list)
for x, line in enumerate(lines):
    xmin = x - 1
    xmax = x + 2
    for match in re.finditer(r"\d+", line):
        ymin = match.start() - 1
        ymax = match.end() + 1
        for x_coord in range(xmin, xmax):
            for y_coord in range(ymin, ymax):
                coord = (x_coord, y_coord)
                if coord in symbol_coords:
                    matches[coord].append(match)

total = 0
for parts in matches.values():
    if len(parts) == 2:
        total += int(parts[0].group(0)) * int(parts[1].group(0))

print(total)
