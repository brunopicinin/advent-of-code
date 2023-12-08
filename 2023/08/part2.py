import re
from itertools import cycle
from math import lcm

# filename = "sample3.txt"
filename = "input.txt"

data = open(filename).read()

instructions, _, *elements = data.splitlines()

node_map = {}
for element in elements:
    start, left, right = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", element)[0]
    node_map[f"{start}L"] = left
    node_map[f"{start}R"] = right

all_steps = []
nodes = {key[:3] for key in node_map if key[:3].endswith("A")}

for node in nodes:
    steps = 0
    for instruction in cycle(instructions):
        steps += 1
        node = node_map[node + instruction]
        if node.endswith("Z"):
            break
    all_steps.append(steps)

print(lcm(*all_steps))
