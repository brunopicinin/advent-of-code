from collections import defaultdict

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().split("\n\n")


def parse_crates(data):
    crates = defaultdict(list)
    data = data.replace("    ", "[-] ")
    data = data.replace(" ", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    lines = reversed(data.splitlines()[:-1])
    for line in lines:
        for i, char in enumerate(line, start=1):
            if char != "-":
                crates[i].append(char)
    return crates


def parse_moves(data):
    for line in data.splitlines():
        _, qty, _, src, _, dst = line.split()
        yield int(qty), int(src), int(dst)


def move(crates, src, dst):
    item = crates[src].pop()
    crates[dst].append(item)


crates = parse_crates(data[0])

for qty, src, dst in parse_moves(data[1]):
    for _ in range(qty):
        move(crates, src, dst)

print("".join(x.pop() for x in crates.values()))
