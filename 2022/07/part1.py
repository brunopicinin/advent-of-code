from collections import defaultdict

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()

curdir = ["<root>"]
tree = defaultdict(int)

for line in data:
    items = line.split()

    if items[0] == "$":
        if items[1] == "cd":
            folder = items[2]
            if folder == "/":
                curdir = ["<root>"]
            elif folder == "..":
                curdir.pop()
            else:
                curdir.append(folder)

    elif items[0] == "dir":
        pass

    else:  # file
        size = int(items[0])
        li = curdir.copy()
        while li:
            tree["/".join(li)] += size
            li.pop()

print(sum(x for x in tree.values() if x <= 100000))
