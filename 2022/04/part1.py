# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read().splitlines()


def elf_sections(assignment):
    start, stop = [int(x) for x in assignment.split("-")]
    return set(range(start, stop + 1))


count = 0
for line in data:
    elf1, elf2 = [elf_sections(x) for x in line.split(",")]
    if elf1 <= elf2 or elf1 >= elf2:
        count += 1

print(count)
