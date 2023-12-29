import sys

sys.setrecursionlimit(10000)

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
        move = (next_x - x, next_y - y)
        match tile, move:
            case ".", _:
                yield (next_x, next_y)
            case "^", (-1, 0):
                yield (next_x, next_y)
            case "v", (1, 0):
                yield (next_x, next_y)
            case "<", (0, -1):
                yield (next_x, next_y)
            case ">", (0, 1):
                yield (next_x, next_y)


def hike_length(point, visited):
    if point == finish:
        return 0

    visited = visited.copy()
    visited.add(point)

    dist = -float("inf")
    for next_point in neighbors(point):
        if next_point not in visited:
            dist = max(dist, hike_length(next_point, visited) + 1)

    return dist


print(hike_length(start, set()))
