import re

# filename = "sample.txt"
filename = "input.txt"


def count_arrangements(records, groups):
    if not is_valid(records, groups):
        return 0
    idx = records.find("?")
    if idx >= 0:
        cnt1 = count_arrangements(records[:idx] + "." + records[idx + 1 :], groups)
        cnt2 = count_arrangements(records[:idx] + "#" + records[idx + 1 :], groups)
        return cnt1 + cnt2
    else:
        return 1 if is_exact(records, groups) else 0


def is_valid(records, groups):
    text = records.strip(".")
    text = re.sub(r"\.+", ".", text)
    return len(text) >= sum(groups) + len(groups) - 1


def is_exact(records, groups):
    matches = re.findall(r"#+", records)
    return groups == tuple(len(m) for m in matches)


data = open(filename).read()

counts = 0

for row in data.splitlines():
    records, groups = row.split()
    groups = tuple(int(x) for x in groups.split(","))
    counts += count_arrangements(records, groups)

print(counts)
