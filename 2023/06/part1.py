from math import ceil, floor, prod, sqrt

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()
time_data, distance_data = data.splitlines()

times = [int(x) for x in time_data.split()[1:]]
distances = [int(x) for x in distance_data.split()[1:]]

ways_to_win = []
for time, distance in zip(times, distances):
    # x^2 -(time)*x + distance < 0
    x1 = floor((time - sqrt(time**2 - 4 * distance)) / 2)
    x2 = ceil((time + sqrt(time**2 - 4 * distance)) / 2)
    ways_to_win.append(x2 - x1 - 1)

print(prod(ways_to_win))
