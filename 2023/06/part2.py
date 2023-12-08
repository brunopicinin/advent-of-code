from math import ceil, floor, sqrt

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
time_data, distance_data = data.splitlines()

time = int("".join(ch for ch in time_data if ch.isdigit()))
distance = int("".join(ch for ch in distance_data if ch.isdigit()))

# x^2 -(time)*x + distance < 0
x1 = floor((time - sqrt(time**2 - 4 * distance)) / 2)
x2 = ceil((time + sqrt(time**2 - 4 * distance)) / 2)
print(x2 - x1 - 1)
