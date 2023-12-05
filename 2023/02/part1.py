# filename = "sample.txt"
filename = "input.txt"

RED = 12
GREEN = 13
BLUE = 14


def count(cube):
    return int("".join(ch for ch in cube if ch.isdigit()))


def is_valid(pick):
    cubes = pick.split(",")
    for cube in cubes:
        if "red" in cube and count(cube) > RED:
            return False
        if "green" in cube and count(cube) > GREEN:
            return False
        if "blue" in cube and count(cube) > BLUE:
            return False
    return True


data = open(filename).read()
total = 0

for line in data.splitlines():
    part1, _, part2 = line.partition(":")
    game = int(part1.split()[1])
    picks = part2.split(";")

    if all(is_valid(pick) for pick in picks):
        total += game

print(total)
