# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
data = list(map(int, data))

count = 0
last = float("inf")

for i, _ in enumerate(data):
    if i == len(data) - 2:
        break
    s = sum(data[i : i + 3])
    if s > last:
        count += 1
    last = s

print(count)
