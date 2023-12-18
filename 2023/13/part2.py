# filename = "sample.txt"
filename = "input.txt"


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def changes(matrix1, matrix2):
    diffs = 0
    for row1, row2 in zip(matrix1, matrix2):
        for val1, val2 in zip(row1, row2):
            if val1 != val2:
                diffs += 1
    return diffs


data = open(filename).read()

patterns = data.split("\n\n")
total = 0

for pattern in patterns:
    matrix = [list(row) for row in pattern.splitlines()]

    n_rows = len(matrix)
    for i in range(1, n_rows):
        if changes(reversed(matrix[:i]), matrix[i:]) == 1:
            total += 100 * i
            break

    matrix = transpose(matrix)

    n_cols = len(matrix)
    for j in range(1, n_cols):
        if changes(reversed(matrix[:j]), matrix[j:]) == 1:
            total += j
            break

print(total)
