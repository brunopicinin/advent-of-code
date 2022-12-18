from dataclasses import dataclass

# filename = "sample1.txt"
filename = "input.txt"

data = open(filename).read().splitlines()
data = [x.split() for x in data]


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(x=self.x + other.x, y=self.y + other.y)

    def follow_dist(self, other):
        touching = abs(other.x - self.x) <= 1 and abs(other.y - self.y) <= 1
        same_row = other.y == self.y
        same_col = other.x == self.x

        dx = (self.x + other.x) // 2 - self.x
        dy = (self.y + other.y) // 2 - self.y

        if touching:
            return Coord(0, 0)
        elif same_row:
            return Coord(dx, 0)
        elif same_col:
            return Coord(0, dy)
        else:  # diagonal
            dd = max(abs(dx), abs(dy))
            dx = dd if dx >= 0 else -dd
            dy = dd if dy >= 0 else -dd
            return Coord(dx, dy)

    def as_tuple(self):
        return (self.x, self.y)


head = Coord(0, 0)
tail = Coord(0, 0)
visited = {tail.as_tuple()}

moves = {
    "R": Coord(1, 0),
    "L": Coord(-1, 0),
    "U": Coord(0, -1),
    "D": Coord(0, 1),
}

for direction, size in data:
    move = moves[direction]
    for _ in range(int(size)):
        head += move
        tail += tail.follow_dist(head)
        visited.add(tail.as_tuple())

print(len(visited))
