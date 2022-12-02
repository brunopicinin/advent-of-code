# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
data = data.split("\n\n")
data = [list(map(int, x.split())) for x in data]

top_cals = sorted((sum(elf) for elf in data), reverse=True)
print(sum(top_cals[:3]))
