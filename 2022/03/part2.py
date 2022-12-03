import string

# filename = "sample.txt"
filename = "input.txt"


def groups_of_three(data):
    args = [iter(data)] * 3
    return zip(*args)


def priority(letter):
    return string.ascii_letters.index(letter) + 1


data = open(filename).read().splitlines()
data = list(groups_of_three(data))

common = []
for group in data:
    first, second, third = group
    common.extend(set(first) & set(second) & set(third))

print(sum(map(priority, common)))
