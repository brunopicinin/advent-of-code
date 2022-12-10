# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

grid = [[int(x) for x in line] for line in data.splitlines()]
rows, cols = len(grid), len(grid[0])

visible = set()


def scan(ivals, jvals, transpose=False):
    for i in ivals:
        tallest = -1
        for j in jvals:
            size = grid[j][i] if transpose else grid[i][j]
            if size > tallest:
                tallest = size
                visible.add((j, i) if transpose else (i, j))


# scan from left
ivals = list(range(rows))
jvals = list(range(cols))
scan(ivals, jvals)

# scan from right
ivals = list(range(rows))
jvals = list(reversed(range(cols)))
scan(ivals, jvals)

# scan from top
ivals = list(range(rows))
jvals = list(range(cols))
scan(ivals, jvals, transpose=True)

# scan from bottom
ivals = list(range(rows))
jvals = list(reversed(range(cols)))
scan(ivals, jvals, transpose=True)

print(len(visible))
