# filename = "sample.txt"
filename = "input.txt"


def convert(map, value):
    for rule in map:
        diff = value - rule["source"]
        if 0 <= diff < rule["range"]:
            return rule["dest"] + diff
    return value


data = open(filename).read()
seeds_data, *maps_data = data.split("\n\n")

seeds = [int(s) for s in seeds_data.split(":")[1].split()]

maps = []
for map_data in maps_data:
    map = []
    lines = map_data.splitlines()[1:]
    for line in lines:
        rule = [int(x) for x in line.split()]
        map.append({"source": rule[1], "range": rule[2], "dest": rule[0]})
    maps.append(map)


locations = []
for value in seeds:
    for map in maps:
        value = convert(map, value)
    locations.append(value)

print(min(locations))
