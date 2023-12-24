import re

# filename = "sample.txt"
filename = "input.txt"


def calc_area(points):
    size = len(points)
    total = 0
    for i in range(size):
        total += points[i][0] * (points[(i + 1) % size][1] - points[(i - 1) % size][1])
    return abs(total // 2)


def calc_boundary(points):
    size = len(points)
    total = 0
    for i in range(size):
        dx = abs(points[i][0] - points[(i + 1) % size][0])
        dy = abs(points[i][1] - points[(i + 1) % size][1])
        total += dx + dy
    return total


def calc_interior(area, boundary):
    return 1 + area - (boundary // 2)


data = open(filename).read()

dirs = {
    "0": (0, 1),
    "1": (1, 0),
    "2": (0, -1),
    "3": (-1, 0),
}
points = [(0, 0)]

for line in data.splitlines():
    match = re.findall(r"\(#(.*)\)", line)[0]
    code, dir_str = match[:-1], match[-1]

    dir = dirs[dir_str]
    meters = int(code, 16)

    last_point = points[-1]
    x = last_point[0] + dir[0] * meters
    y = last_point[1] + dir[1] * meters
    points.append((x, y))

area = calc_area(points)
boundary = calc_boundary(points)
interior = calc_interior(area, boundary)

print(boundary + interior)
