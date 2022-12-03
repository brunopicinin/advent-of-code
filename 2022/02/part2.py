# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

data = data.replace("A", "rock")
data = data.replace("B", "paper")
data = data.replace("C", "scissors")
data = data.replace("X", "lose")
data = data.replace("Y", "draw")
data = data.replace("Z", "win")

data = [x.split() for x in data.splitlines()]


def score1(they, me):
    if me == "draw":
        choice = they
    elif me == "lose":
        choice = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }[they]
    elif me == "win":
        choice = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock",
        }[they]

    return {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }[choice]


def score2(me):
    return {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }[me]


total = 0
for they, me in data:
    total += score1(they, me) + score2(me)

print(total)
