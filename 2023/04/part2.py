# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

cards = []

for line in data.splitlines():
    games = line.split(":")[1]
    left, right = games.split("|")

    win_nums = {int(x) for x in left.split()}
    my_nums = {int(x) for x in right.split()}

    count = len(win_nums & my_nums)
    cards.append([1, count])


for i, [have, winning] in enumerate(cards):
    for _ in range(have):
        for x in range(1, winning + 1):
            cards[i + x][0] += 1

print(sum(x[0] for x in cards))
