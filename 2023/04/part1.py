# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

total = 0

for line in data.splitlines():
    games = line.split(":")[1]
    left, right = games.split("|")

    win_nums = {int(x) for x in left.split()}
    my_nums = {int(x) for x in right.split()}

    count = len(win_nums & my_nums) - 1
    total += 2**count if count >= 0 else 0

print(total)
