from itertools import pairwise

# filename = "sample.txt"
filename = "input.txt"


def diffs(values):
    return [y - x for x, y in pairwise(values)]


data = open(filename).read()

predictions = []

for history in data.splitlines():
    values = [int(x) for x in history.split()]
    firsts = []

    while any(values):
        firsts.append(values[0])
        values = diffs(values)

    pred = 0
    for value in reversed(firsts):
        pred = value - pred

    predictions.append(pred)

print(sum(predictions))
