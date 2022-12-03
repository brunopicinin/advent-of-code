# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

data = data.replace("A", "rock")
data = data.replace("B", "paper")
data = data.replace("C", "scissors")
data = data.replace("X", "rock")
data = data.replace("Y", "paper")
data = data.replace("Z", "scissors")

data = [x.split() for x in data.splitlines()]


def score1(they, me):
    loose = (
        (they == "rock" and me == "scissors")
        or (they == "paper" and me == "rock")
        or (they == "scissors" and me == "paper")
    )
    draw = they == me

    if loose:
        return 0
    elif draw:
        return 3
    else:
        return 6


def score2(me):
    return {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }[me]


total = 0
for they, me in data:
    total += score1(they, me) + score2(me)

print(total)
