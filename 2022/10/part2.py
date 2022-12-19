# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
data = [x.split() for x in data]

X = [1]


def add_to_register(val):
    X.append(X[-1] + val)


for instruction in data:
    if instruction[0] == "noop":
        add_to_register(0)
    else:  # addx
        val = int(instruction[1])
        add_to_register(0)
        add_to_register(val)

for i in range(240):
    x = X[i]
    if x - 1 <= i % 40 <= x + 1:
        print("#", end="")
    else:
        print(".", end="")
    if i % 40 == 39:
        print()
