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
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
points = [(0, 0)]

for line in data.splitlines():
    dir_str, meters_str, _ = line.split()
    dir = dirs[dir_str]
    meters = int(meters_str)

    last_point = points[-1]
    x = last_point[0] + dir[0] * meters
    y = last_point[1] + dir[1] * meters
    points.append((x, y))

area = calc_area(points)
boundary = calc_boundary(points)
interior = calc_interior(area, boundary)

print(boundary + interior)
