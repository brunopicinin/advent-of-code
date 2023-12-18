# filename = "sample.txt"
filename = "input.txt"


def rotate_left(matrix):
    return rotate_right(rotate_right(rotate_right(matrix)))


def rotate_right(matrix):
    return tuple(tuple(reversed(items)) for items in zip(*matrix))


def cycle(matrix):
    for _ in range(4):
        matrix = rotate_right(slide_left(row) for row in matrix)
    return matrix


def slide_left(row):
    row = "".join(row)
    while ".O" in row:
        row = row.replace(".O", "O.")
    return tuple(row)


def find_cycle_size(graph, key):
    seen = set()
    while True:
        try:
            value = graph[key]
        except KeyError:
            return 0
        if value in seen:
            return len(seen)
        else:
            seen.add(value)
            key = value


data = open(filename).read()

matrix = tuple(tuple(row) for row in data.splitlines())
matrix = rotate_left(matrix)


graph = {}

for i in range(1, 1000000001):
    new_matrix = cycle(matrix)
    graph[matrix] = new_matrix
    matrix = new_matrix

    cycle_size = find_cycle_size(graph, matrix)
    if cycle_size:
        missing_cycles = 1000000000 - i
        for _ in range(missing_cycles % cycle_size):
            matrix = cycle(matrix)
        break


matrix = rotate_right(matrix)
total = 0

for i, row in enumerate(reversed(matrix), start=1):
    total += i * row.count("O")

print(total)
