from heapq import heappop, heappush

# filename = "sample.txt"
filename = "input.txt"

vert = 0
horiz = 1


def least_heat_loss(matrix):
    visited = set()
    queue = []
    heappush(queue, (0, (0, 0, vert)))
    heappush(queue, (0, (0, 0, horiz)))

    while queue:
        cost, (row, col, dir) = heappop(queue)

        if (row, col) == (last_row, last_col):
            break

        if (row, col, dir) in visited:
            continue

        visited.add((row, col, dir))

        next_dir = horiz if dir == vert else vert
        orig_node_cost = cost

        for i in range(1, 4):
            next_row = row - i if dir == vert else row
            next_col = col - i if dir == horiz else col

            if next_col < 0 or next_row < 0:
                break

            cost += matrix[next_row][next_col]

            if ((next_row, next_col, next_dir)) not in visited:
                heappush(queue, (cost, (next_row, next_col, next_dir)))

        cost = orig_node_cost
        for i in range(1, 4):
            next_row = row + i if dir == vert else row
            next_col = col + i if dir == horiz else col

            if next_col > last_col or next_row > last_row:
                break

            cost += matrix[next_row][next_col]

            if ((next_row, next_col, next_dir)) not in visited:
                heappush(queue, (cost, (next_row, next_col, next_dir)))

    return cost


data = open(filename).read()

matrix = [[int(x) for x in row] for row in data.splitlines()]
last_row = len(matrix) - 1
last_col = len(matrix[0]) - 1

print(least_heat_loss(matrix))
