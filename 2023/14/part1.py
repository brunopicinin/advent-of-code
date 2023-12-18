# filename = "sample.txt"
filename = "input.txt"


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def slide_left(row):
    row = "".join(row)
    while ".O" in row:
        row = row.replace(".O", "O.")
    return list(row)


data = open(filename).read()

matrix = [list(row) for row in data.splitlines()]

matrix = transpose(matrix)
matrix = [slide_left(row) for row in matrix]
matrix = transpose(matrix)

total = 0

for i, row in enumerate(reversed(matrix), start=1):
    total += i * row.count("O")

print(total)
