# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
data = data.split("\n\n")
data = [list(map(int, x.split())) for x in data]

most_cals = 0
for elf in data:
    cals = sum(elf)
    most_cals = max(cals, most_cals)

print(most_cals)
