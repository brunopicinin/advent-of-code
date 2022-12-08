# filename = "sample1.txt"
# filename = "sample2.txt"
# filename = "sample3.txt"
# filename = "sample4.txt"
# filename = "sample5.txt"
filename = "input.txt"

data = open(filename).read().strip()

for i, _ in enumerate(data[3:]):
    chars = data[i : i + 4]
    if len(set(chars)) == 4:
        print(i + 4)
        break
