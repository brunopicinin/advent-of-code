from collections import Counter

# filename = "sample.txt"
filename = "input.txt"

card_values = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def key_fn(hand):
    values = [card_values[card] for card in hand]
    return [get_type(hand)] + values


def get_type(hand):
    new_hand = hand.replace("J", "")
    counts = [mc[1] for mc in Counter(new_hand).most_common()]
    if counts:
        counts[0] += len(hand) - len(new_hand)  # jokers
    else:
        return 7  # five Js
    match counts:
        case [1, 1, 1, 1, 1]:
            return 1  # high card
        case [2, 1, 1, 1]:
            return 2  # one pair
        case [2, 2, 1]:
            return 3  # two pair
        case [3, 1, 1]:
            return 4  # three of a kind
        case [3, 2]:
            return 5  # full house
        case [4, 1]:
            return 6  # four of a kind
        case [5]:
            return 7  # five of a kind


data = open(filename).read()

hands = {}
for line in data.splitlines():
    hand, bid = line.split()
    hands[hand] = int(bid)

sorted_hands = sorted(hands, key=key_fn)

winnings = 0
for rank, hand in enumerate(sorted_hands, start=1):
    bid = hands[hand]
    winnings += rank * bid

print(winnings)
