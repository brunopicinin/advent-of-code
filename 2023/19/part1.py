import operator
import re

# filename = "sample.txt"
filename = "input.txt"


def create_process_func(conds, last):
    rules = []
    for cond in conds:
        category, op, value, wkfl_name = re.findall(r"([xmas])([<>])(\d+):(.*)", cond)[0]
        comparison = operator.gt if op == ">" else operator.lt
        threshold = int(value)
        rules.append((category, comparison, threshold, wkfl_name))

    def process(part):
        for category, comparison, threshold, wkfl_name in rules:
            if comparison(part[category], threshold):
                return wkfl_name
        return last

    return process


def process_part(workflow_map, part):
    wkfl_name = "in"
    while wkfl_name not in ("A", "R"):
        func = workflow_map[wkfl_name]
        wkfl_name = func(part)
    return wkfl_name


data = open(filename).read()

workflows, parts = data.split("\n\n")

workflow_map = {}

for workflow in workflows.splitlines():
    name, rules = re.findall(r"(.*){(.*)}", workflow)[0]
    *conds, last = rules.split(",")
    workflow_map[name] = create_process_func(conds, last)

total = 0

for part in parts.splitlines():
    x, m, a, s = re.findall(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part)[0]
    ratings = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
    if process_part(workflow_map, ratings) == "A":
        total += sum(ratings.values())

print(total)
