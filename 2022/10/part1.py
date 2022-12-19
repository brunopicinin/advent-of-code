# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
data = [x.split() for x in data]

cycle = 0
X = 1
strengths = 0


def check_cycle():
    global strengths
    if cycle in (20, 60, 100, 140, 180, 220):
        strengths += cycle * X


def add_to_register(val):
    global cycle, X
    cycle += 1
    check_cycle()
    X += val


for instruction in data:
    if instruction[0] == "noop":
        add_to_register(0)
    else:  # addx
        val = int(instruction[1])
        add_to_register(0)
        add_to_register(val)

print(strengths)
