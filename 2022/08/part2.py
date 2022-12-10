# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

grid = [[int(x) for x in line] for line in data.splitlines()]
rows, cols = len(grid), len(grid[0])


def empty_grid():
    return [[0 for _ in range(cols)] for _ in range(rows)]


# scan from left
score1 = empty_grid()
for i in range(rows):
    lastpos = {k: 0 for k in range(10)}
    for j in range(cols):
        size = grid[i][j]
        taller_pos = max(lastpos[k] for k in range(size, 10))
        score1[i][j] = j - taller_pos
        lastpos[size] = j

# scan from right
score2 = empty_grid()
for i in range(rows):
    lastpos = {k: cols - 1 for k in range(10)}
    for j in reversed(range(cols)):
        size = grid[i][j]
        taller_pos = min(lastpos[k] for k in range(size, 10))
        score2[i][j] = taller_pos - j
        lastpos[size] = j

# scan from top
score3 = empty_grid()
for i in range(rows):
    lastpos = {k: 0 for k in range(10)}
    for j in range(cols):
        size = grid[j][i]
        taller_pos = max(lastpos[k] for k in range(size, 10))
        score3[j][i] = j - taller_pos
        lastpos[size] = j

# scan from bottom
score4 = empty_grid()
for i in range(rows):
    lastpos = {k: cols - 1 for k in range(10)}
    for j in reversed(range(cols)):
        size = grid[j][i]
        taller_pos = min(lastpos[k] for k in range(size, 10))
        score4[j][i] = taller_pos - j
        lastpos[size] = j

scenic_score = empty_grid()
for i in range(rows):
    for j in range(cols):
        scenic_score[i][j] = score1[i][j] * score2[i][j] * score3[i][j] * score4[i][j]

print(max(s for scores in scenic_score for s in scores))
