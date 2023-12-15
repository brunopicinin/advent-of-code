from itertools import pairwise

# filename = "sample.txt"
filename = "input.txt"


def diffs(values):
    return [y - x for x, y in pairwise(values)]


data = open(filename).read()

predictions = []

for history in data.splitlines():
    values = [int(x) for x in history.split()]
    lasts = []
    while any(values):
        lasts.append(values[-1])
        values = diffs(values)
    predictions.append(sum(lasts))

print(sum(predictions))
