# filename = "sample.txt"
filename = "input.txt"


def HASH(string):
    value = 0
    for code in map(ord, string):
        value += code
        value *= 17
        value %= 256
    return value


data = open(filename).read()

steps = data.strip().split(",")

print(sum(HASH(step) for step in steps))
