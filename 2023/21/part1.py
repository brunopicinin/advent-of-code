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
            if x < 0 or y < 0 or x > last_row or y > last_col:
                continue
            if matrix[x][y] == "#":
                continue
            yield (x, y)


data = open(filename).read()

matrix = [list(row) for row in data.splitlines()]
last_row = len(matrix) - 1
last_col = len(matrix[0]) - 1

plots = [find_start(matrix)]

for _ in range(64):
    plots = set(next_plots(matrix, plots))

print(len(plots))
