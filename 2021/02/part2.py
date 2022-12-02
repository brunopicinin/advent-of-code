# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()

horizontal, depth, aim = 0, 0, 0

for line in data:
    cmd, val = line.split()
    val = int(val)
    if cmd == "forward":
        horizontal += val
        depth += val * aim
    elif cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val

print(horizontal * depth)
