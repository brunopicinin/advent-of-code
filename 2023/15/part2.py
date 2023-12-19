from collections import defaultdict

# filename = "sample.txt"
filename = "input.txt"


def HASH(string):
    value = 0
    for code in map(ord, string):
        value += code
        value *= 17
        value %= 256
    return value


def find(box, label):
    labels = [lens[0] for lens in box]
    try:
        return labels.index(label)
    except ValueError:
        return -1


data = open(filename).read()

steps = data.strip().split(",")
boxes = defaultdict(list)

for step in steps:
    label, operation, focal_length = step.partition("=") if "=" in step else step.partition("-")
    box = boxes[HASH(label)]
    idx = find(box, label)

    match operation, idx >= 0:
        case "=", True:
            box[idx][1] = int(focal_length)
        case "=", False:
            box.append([label, int(focal_length)])
        case "-", True:
            del box[idx]

focusing_power = 0

for boxnum, lenses in boxes.items():
    for pos, lens in enumerate(lenses, start=1):
        focusing_power += (boxnum + 1) * pos * lens[1]

print(focusing_power)
