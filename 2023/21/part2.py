from itertools import pairwise

# filename = "sample.txt"
filename = "input.txt"


def find_start(matrix):
    for x, row in enumerate(matrix):
        for y, val in enumerate(row):
            if val == "S":
                return (x, y)


def next_plots(matrix, curr_plots):
    for curr_x, curr_y in curr_plots:
        nexts = [
            (curr_x + 1, curr_y),
            (curr_x - 1, curr_y),
            (curr_x, curr_y + 1),
            (curr_x, curr_y - 1),
        ]
        for x, y in nexts:
            if matrix[x % n_rows][y % n_cols] == "#":
                continue
            yield (x, y)


def diffs(values):
    return [y - x for x, y in pairwise(values)]


def predict_next_value(values):
    lasts = []
    while any(values):
        lasts.append(values[-1])
        values = diffs(values)
    return sum(lasts)


data = open(filename).read()

matrix = [list(row) for row in data.splitlines()]
n_rows = len(matrix)
n_cols = len(matrix[0])

start = find_start(matrix)
values = []

plots = [start]
for _ in range(65 + 0 * 131):
    plots = set(next_plots(matrix, plots))
values.append(len(plots))

plots = [start]
for _ in range(65 + 1 * 131):
    plots = set(next_plots(matrix, plots))
values.append(len(plots))

plots = [start]
for _ in range(65 + 2 * 131):
    plots = set(next_plots(matrix, plots))
values.append(len(plots))

for _ in range(202300 - len(values) + 1):
    next_value = predict_next_value(values)
    values = values[1:] + [next_value]

print(next_value)
