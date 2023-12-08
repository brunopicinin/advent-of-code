import re
from itertools import cycle

# filename = "sample1.txt"
# filename = "sample2.txt"
filename = "input.txt"

data = open(filename).read()

instructions, _, *elements = data.splitlines()

node_map = {}
for element in elements:
    start, left, right = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", element)[0]
    node_map[f"{start}L"] = left
    node_map[f"{start}R"] = right

steps = 0
node = "AAA"

for instruction in cycle(instructions):
    steps += 1
    node = node_map[node + instruction]
    if node == "ZZZ":
        break

print(steps)
