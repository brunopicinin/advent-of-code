# filename = "sample.txt"
filename = "input.txt"


def transpose(matrix):
    return list(map(list, zip(*matrix)))


data = open(filename).read()

patterns = data.split("\n\n")
total = 0

for pattern in patterns:
    matrix = [list(row) for row in pattern.splitlines()]

    n_rows = len(matrix)
    for i in range(1, n_rows):
        if all(row1 == row2 for row1, row2 in zip(reversed(matrix[:i]), matrix[i:])):
            total += 100 * i
            break

    matrix = transpose(matrix)

    n_cols = len(matrix)
    for j in range(1, n_cols):
        if all(col1 == col2 for col1, col2 in zip(reversed(matrix[:j]), matrix[j:])):
            total += j
            break

print(total)
