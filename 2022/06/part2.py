# filename = "sample1.txt"
# filename = "sample2.txt"
# filename = "sample3.txt"
# filename = "sample4.txt"
# filename = "sample5.txt"
filename = "input.txt"

data = open(filename).read().strip()

for i, _ in enumerate(data[13:]):
    chars = data[i : i + 14]
    if len(set(chars)) == 14:
        print(i + 14)
        break
