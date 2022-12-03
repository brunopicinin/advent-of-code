import string

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()


def priority(letter):
    return string.ascii_letters.index(letter) + 1


both = []
for rucksack in data:
    size = len(rucksack) // 2
    first, second = rucksack[:size], rucksack[size:]
    both.extend(set(first) & set(second))

print(sum(map(priority, both)))
