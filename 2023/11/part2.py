from itertools import combinations

# filename = "sample.txt"
filename = "input.txt"


def annotate_dists(data):
    return [[[val, 1, 1] for val in row] for row in data]


def expand(data, dim):
    for row in data:
        if all(c[0] == "." for c in row):
            for c in row:
                c[dim] = 1000000
    return data


def transpose(data):
    return list(map(list, zip(*data)))


def find_galaxies(data):
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val[0] == "#":
                yield (i, j)


def distance(universe, g1, g2):
    total = 0

    x_start = min(g1[0], g2[0])
    x_stop = max(g1[0], g2[0])
    for x in range(x_start, x_stop):
        total += universe[x][0][1]

    y_start = min(g1[1], g2[1])
    y_stop = max(g1[1], g2[1])
    for y in range(y_start, y_stop):
        total += universe[0][y][2]

    return total


data = open(filename).read()

universe = [list(row) for row in data.splitlines()]
universe = annotate_dists(universe)
expanded_universe = transpose(expand(transpose(expand(universe, dim=1)), dim=2))

galaxies = find_galaxies(expanded_universe)
pairs = combinations(galaxies, 2)

print(sum(distance(universe, *pair) for pair in pairs))
