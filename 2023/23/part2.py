from collections import defaultdict

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

matrix = [list(row) for row in data.splitlines()]
last_row = len(matrix) - 1
last_col = len(matrix[0]) - 1

start = (0, matrix[0].index("."))
finish = (last_row, matrix[last_row].index("."))


def neighbors(point):
    x, y = point
    possibilities = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    for next_x, next_y in possibilities:
        if next_x < 0 or next_y < 0 or next_x > last_row or next_y > last_col:
            continue
        tile = matrix[next_x][next_y]
        if tile == "#":
            continue
        yield (next_x, next_y)


def find_graph_nodes(matrix):
    nodes = [start]
    for x, row in enumerate(matrix):
        for y, tile in enumerate(row):
            if tile == "#":
                continue
            point = (x, y)
            if len(list(neighbors(point))) > 2:
                nodes.append(point)
    return nodes + [finish]


nodes = find_graph_nodes(matrix)


def find_node_distances(nodes):
    distances = defaultdict(dict)

    for node in nodes:
        visited = {node}
        dists = [(node, 0)]

        while dists:
            point, dist = dists.pop()

            if dist > 0 and point in nodes:
                distances[node][point] = dist
                continue

            for next_point in neighbors(point):
                if next_point not in visited:
                    visited.add(next_point)
                    dists.append((next_point, dist + 1))

    return distances


distances = find_node_distances(nodes)


def hike_length(point, visited):
    if point == finish:
        return 0

    visited = visited.copy()
    visited.add(point)

    dist = -float("inf")
    for next_point, next_dist in distances[point].items():
        if next_point not in visited:
            dist = max(dist, hike_length(next_point, visited) + next_dist)

    return dist


print(hike_length(start, set()))
