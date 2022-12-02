# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()

horizontal, depth = 0, 0

for line in data:
    cmd, val = line.split()
    val = int(val)
    if cmd == "forward":
        horizontal += val
    elif cmd == "down":
        depth += val
    elif cmd == "up":
        depth -= val

print(horizontal * depth)
