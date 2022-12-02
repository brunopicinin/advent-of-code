# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()


def most_common_bit(lines, col):
    rows = len(lines)
    bits = [int(x[col]) for x in lines]
    s = sum(bits)
    if s >= rows / 2:
        return "1"
    else:
        return "0"


def least_common_bit(lines, col):
    rows = len(lines)
    bits = [int(x[col]) for x in lines]
    s = sum(bits)
    if s >= rows / 2:
        return "0"
    else:
        return "1"


cols = len(data[0])

lines = data[:]
for c in range(cols):
    bit = most_common_bit(lines, c)
    lines = [l for l in lines if l[c] == bit]
    if len(lines) == 1:
        break

oxygen = int("".join(lines), 2)

lines = data[:]
for c in range(cols):
    bit = least_common_bit(lines, c)
    lines = [l for l in lines if l[c] == bit]
    if len(lines) == 1:
        break

co2 = int("".join(lines), 2)

print(oxygen * co2)
