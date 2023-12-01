# filename = "sample1.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
digits = [[ch for ch in line if ch.isdigit()] for line in data]
nums = [int(dg[0] + dg[-1]) for dg in digits]

print(sum(nums))
