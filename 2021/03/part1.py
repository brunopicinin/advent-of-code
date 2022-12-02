# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()

rows = len(data)
cols = len(data[0])

gamma, epsilon = [], []

for c in range(cols):
    bits = [int(x[c]) for x in data]
    s = sum(bits)
    if s > rows / 2:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")


gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma * epsilon)
