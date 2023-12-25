import math
import sys
from collections import deque

filename = "input.txt"


class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = "off"

    def receive(self, sender, pulse):
        if pulse == "low":
            self.state = "on" if self.state == "off" else "off"
            new_pulse = "high" if self.state == "on" else "low"
            for output in self.outputs:
                yield (self.name, output, new_pulse)


class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = {}

    def receive(self, sender, pulse):
        self.state[sender] = pulse
        new_pulse = "low" if set(self.state.values()) == {"high"} else "high"
        for output in self.outputs:
            yield (self.name, output, new_pulse)


class Broadcast:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def receive(self, sender, pulse):
        raise NotImplementedError


class Output:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def receive(self, sender, pulse):
        return []


data = open(filename).read()

modules = {
    "output": Output("output", []),
    "rx": Output("rx", []),
}

for line in data.splitlines():
    input, output = line.split(" -> ")
    type, name = input[0], input[1:]
    outputs = output.split(", ")

    if type == "%":
        modules[name] = FlipFlop(name, outputs)
    elif type == "&":
        modules[name] = Conjunction(name, outputs)
    else:
        modules["broadcaster"] = Broadcast("broadcaster", outputs)

for name, module in modules.items():
    for output in module.outputs:
        input = modules.get(output)
        if input and isinstance(input, Conjunction):
            input.state[name] = "low"

presses_per_input = {name: 0 for name, module in modules.items() if "vr" in module.outputs}
presses_total = 0

while True:
    queue = deque([("broadcaster", output, "low") for output in modules["broadcaster"].outputs])
    presses_total += 1

    while queue:
        name, output, pulse = queue.popleft()

        module = modules[output]

        if module.name == "vr" and pulse == "high":
            if presses_per_input[name] == 0:
                presses_per_input[name] = presses_total

            if all(presses_per_input.values()):
                print(math.lcm(*presses_per_input.values()))
                sys.exit()

        for task in module.receive(name, pulse):
            queue.append(task)
