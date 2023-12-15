from math import ceil


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


left = Point(0, -1)
right = Point(0, 1)
up = Point(-1, 0)
down = Point(1, 0)

# filename, s_shape, first_move = "sample1.txt", "F", right
# filename, s_shape, first_move = "sample2.txt", "F", right
filename, s_shape, first_move = "input.txt", "7", down


def next_pos(matrix, curr, last):
    current = matrix[curr.x][curr.y]
    diff = curr - last
    match current:
        case "|" if diff == up:
            return curr + up
        case "|" if diff == down:
            return curr + down
        case "-" if diff == left:
            return curr + left
        case "-" if diff == right:
            return curr + right
        case "L" if diff == left:
            return curr + up
        case "L" if diff == down:
            return curr + right
        case "J" if diff == right:
            return curr + up
        case "J" if diff == down:
            return curr + left
        case "7" if diff == right:
            return curr + down
        case "7" if diff == up:
            return curr + left
        case "F" if diff == left:
            return curr + down
        case "F" if diff == up:
            return curr + right


data = open(filename).read()

size = len(data.splitlines()[0]) + 1  # '\n'
s_idx = data.index("S")
s_pos = Point(s_idx // size, s_idx % size)

data = data.replace("S", s_shape)
lines = data.splitlines()

curr_pos, last_pos = s_pos + first_move, s_pos
visited = [curr_pos, last_pos]

while True:
    curr_pos, last_pos = next_pos(lines, curr_pos, last_pos), curr_pos
    if curr_pos in visited:
        break
    visited.append(curr_pos)

print(ceil(len(visited) / 2))
