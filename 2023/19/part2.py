import math
import re

# filename = "sample.txt"
filename = "input.txt"


def create_wkfl_rules(conds):
    rules = []
    for cond in conds:
        category, comparison, value, wkfl_name = re.findall(r"([xmas])([<>])(\d+):(.*)", cond)[0]
        threshold = int(value)
        rules.append((category, comparison, threshold, wkfl_name))
    return rules


def count_accepted(intervals, name):
    if name == "R":
        return 0

    if name == "A":
        return math.prod(end - begin + 1 for begin, end in intervals.values())

    wkfl_rules, last = workflow_map[name]
    total = 0

    for category, comparison, threshold, wkfl_name in wkfl_rules:
        begin, end = intervals[category]

        if comparison == "<":
            accepted = (begin, min(threshold - 1, end))
            rejected = (max(threshold, begin), end)
        else:
            accepted = (max(threshold + 1, begin), end)
            rejected = (begin, min(threshold, end))

        if accepted[0] <= accepted[1]:
            intervals = intervals.copy()
            intervals[category] = accepted
            total += count_accepted(intervals, wkfl_name)

        if rejected[0] <= rejected[1]:
            intervals = intervals.copy()
            intervals[category] = rejected
        else:
            break

    else:
        total += count_accepted(intervals, last)

    return total


data = open(filename).read()

workflows, _ = data.split("\n\n")

workflow_map = {}

for workflow in workflows.splitlines():
    name, rules = re.findall(r"(.*){(.*)}", workflow)[0]
    *conds, last = rules.split(",")
    workflow_map[name] = (create_wkfl_rules(conds), last)

intervals = {rating: (1, 4000) for rating in "xmas"}

print(count_accepted(intervals, "in"))
