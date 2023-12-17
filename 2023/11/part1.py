from itertools import combinations

# filename = "sample.txt"
filename = "input.txt"


def expand(data):
    rows = []
    for row in data:
        rows.append(row)
        if all(c == "." for c in row):
            rows.append(row)
    return rows


def transpose(data):
    return list(map(list, zip(*data)))


def find_galaxies(data):
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == "#":
                yield (i, j)


def distance(g1, g2):
    xdist = abs(g2[0] - g1[0])
    ydist = abs(g2[1] - g1[1])
    return xdist + ydist


data = open(filename).read()

universe = [list(row) for row in data.splitlines()]
expanded_universe = transpose(expand(transpose(expand(universe))))

galaxies = find_galaxies(expanded_universe)
pairs = combinations(galaxies, 2)

print(sum(distance(*pair) for pair in pairs))
