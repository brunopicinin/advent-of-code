from itertools import combinations

# filename, limits = "sample.txt", (7, 27)
filename, limits = "input.txt", (200000000000000, 400000000000000)

data = open(filename).read()

hailstone_lines = []
for line in data.splitlines():
    px, py, _, vx, vy, _ = map(int, line.replace("@", ",").split(","))
    line = (
        (px, py),
        (px + vx, py + vy),
    )
    hailstone_lines.append(line)


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(xdiff, ydiff)
    if div == 0:
        raise ValueError

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


total = 0

for line1, line2 in combinations(hailstone_lines, 2):
    try:
        x, y = intersection(line1, line2)
    except ValueError:
        continue

    if not limits[0] <= x <= limits[1]:
        continue

    if not limits[0] <= y <= limits[1]:
        continue

    px, py = line1[0]
    vx, vy = (line1[1][0] - px, line1[1][1] - py)
    if (x - px) * vx < 0 or (y - py) * vy < 0:
        continue

    px, py = line2[0]
    vx, vy = (line2[1][0] - px, line2[1][1] - py)
    if (x - px) * vx < 0 or (y - py) * vy < 0:
        continue

    total += 1

print(total)
