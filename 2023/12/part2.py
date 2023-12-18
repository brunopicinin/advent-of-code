from functools import cache

# filename = "sample.txt"
filename = "input.txt"


@cache
def count_arrangements(records, groups):
    if not records:
        return 1 if not groups else 0

    if not groups:
        return 1 if "#" not in records else 0

    match records[0]:
        case ".":
            return count_arrangements(records[1:], groups)
        case "?":
            cnt1 = count_arrangements("." + records[1:], groups)
            cnt2 = count_arrangements("#" + records[1:], groups)
            return cnt1 + cnt2
        case "#":
            first = groups[0]
            if len(records) < first:
                return 0
            if "." in records[:first]:
                return 0
            if len(records) > first and records[first] == "#":
                return 0
            return count_arrangements(records[first + 1 :], groups[1:])


data = open(filename).read()

counts = 0

for row in data.splitlines():
    records, groups = row.split()
    records = "?".join([records] * 5)
    groups = ",".join([groups] * 5)
    groups = tuple(int(x) for x in groups.split(","))
    counts += count_arrangements(records, groups)

print(counts)
