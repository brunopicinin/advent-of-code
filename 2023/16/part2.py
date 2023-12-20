import sys

sys.setrecursionlimit(10000)

# filename = "sample.txt"
filename = "input.txt"

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)


def find_next_moves(position, dir):
    if (position, dir) in seen_moves:
        return set()
    else:
        seen_moves.add((position, dir))

    row, col = position

    if row < 0 or col < 0 or row >= n_rows or col >= n_cols:
        return set()

    tile = matrix[row][col]
    moves = {position}

    if (tile == "/" and dir == down) or (tile == "\\" and dir == up):  # go left
        pos = (row + left[0], col + left[1])
        moves |= find_next_moves(pos, left)

    if (tile == "/" and dir == up) or (tile == "\\" and dir == down):  # go right
        pos = (row + right[0], col + right[1])
        moves |= find_next_moves(pos, right)

    if (tile == "/" and dir == right) or (tile == "\\" and dir == left):  # go up
        pos = (row + up[0], col + up[1])
        moves |= find_next_moves(pos, up)

    if (tile == "/" and dir == left) or (tile == "\\" and dir == right):  # go down
        pos = (row + down[0], col + down[1])
        moves |= find_next_moves(pos, down)

    if tile == "." or (tile == "|" and dir in (up, down)) or (tile == "-" and dir in (left, right)):
        pos = (row + dir[0], col + dir[1])
        moves |= find_next_moves(pos, dir)

    if tile == "|" and dir in (left, right):  # go up + down
        pos = (row + up[0], col + up[1])
        moves |= find_next_moves(pos, up)
        pos = (row + down[0], col + down[1])
        moves |= find_next_moves(pos, down)

    if tile == "-" and dir in (up, down):  # go left + right
        pos = (row + left[0], col + left[1])
        moves |= find_next_moves(pos, left)
        pos = (row + right[0], col + right[1])
        moves |= find_next_moves(pos, right)

    return moves


data = open(filename).read()

matrix = [list(row) for row in data.splitlines()]
n_rows = len(matrix)
n_cols = len(matrix[0])

largest = -1

for col in range(n_cols):
    # top row
    seen_moves = set()
    largest = max(largest, len(find_next_moves((0, col), down)))

    # bottom row
    seen_moves = set()
    largest = max(largest, len(find_next_moves((n_rows - 1, col), up)))

for row in range(n_rows):
    # leftmost column
    seen_moves = set()
    largest = max(largest, len(find_next_moves((row, 0), right)))

    # rightmost column
    largest = max(largest, len(find_next_moves((row, n_cols - 1), left)))
    seen_moves = set()

print(largest)
