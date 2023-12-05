# filename = "sample.txt"
filename = "input.txt"


def count(cube):
    return int("".join(ch for ch in cube if ch.isdigit()))


def power(picks):
    red = 0
    green = 0
    blue = 0

    for pick in picks:
        cubes = pick.split(",")
        for cube in cubes:
            cnt = count(cube)
            if "red" in cube:
                red = max(red, cnt)
            if "green" in cube:
                green = max(green, cnt)
            if "blue" in cube:
                blue = max(blue, cnt)

    return red * green * blue


data = open(filename).read()
total = 0

for line in data.splitlines():
    _, _, part2 = line.partition(":")
    picks = part2.split(";")
    total += power(picks)

print(total)
