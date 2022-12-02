# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
data = list(map(int, data))

count = 0
last = float("inf")

for x in data:
    if x > last:
        count += 1
    last = x

print(count)
