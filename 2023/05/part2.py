import sys
from itertools import batched, count

# filename = "sample.txt"
filename = "input.txt"


def convert_back(map, value):
    for rule in map:
        diff = value - rule["dest"]
        if 0 <= diff < rule["range"]:
            return rule["source"] + diff
    return value


data = open(filename).read()
seeds_data, *maps_data = data.split("\n\n")

seeds_pairs = [int(s) for s in seeds_data.split(":")[1].split()]
seed_intervals = {(start, start + count) for start, count in batched(seeds_pairs, 2)}

maps = []
for map_data in maps_data:
    map = []
    lines = map_data.splitlines()[1:]
    for line in lines:
        rule = [int(x) for x in line.split()]
        map.append({"source": rule[1], "range": rule[2], "dest": rule[0]})
    maps.append(map)

for location in count():
    value = location
    for map in reversed(maps):
        value = convert_back(map, value)
    for interval in seed_intervals:
        if interval[0] <= value < interval[1]:
            print(location)
            sys.exit()
