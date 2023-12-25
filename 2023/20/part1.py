from collections import deque

# filename = "sample1.txt"
# filename = "sample2.txt"
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

low = 0
high = 0

for _ in range(1000):
    low += 1  # button push
    queue = deque([("broadcaster", output, "low") for output in modules["broadcaster"].outputs])

    while queue:
        name, output, pulse = queue.popleft()

        if pulse == "low":
            low += 1
        else:
            high += 1

        module = modules[output]
        for task in module.receive(name, pulse):
            queue.append(task)

print(low * high)
