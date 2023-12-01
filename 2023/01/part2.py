# filename = "sample2.txt"
filename = "input.txt"

digits = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]

data = open(filename).read()

nums = []

for line in data.splitlines():
    left_pos = float("inf")
    left_digit = None
    right_pos = -1
    right_digit = None

    for text, digit in digits:
        lpos = line.find(text)
        if 0 <= lpos < left_pos:
            left_pos = lpos
            left_digit = digit

        rpos = line.rfind(text)
        if right_pos < rpos:
            right_pos = rpos
            right_digit = digit

    nums.append(int(left_digit + right_digit))

print(sum(nums))
