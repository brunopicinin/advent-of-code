from collections import defaultdict, deque
from dataclasses import dataclass
from operator import attrgetter

# filename = "sample.txt"
filename = "input.txt"


@dataclass(unsafe_hash=True)
class Brick:
    name: str
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int

    def __repr__(self):
        return self.name

    def supports(self, other):
        self_coords = set()
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                self_coords.add((x, y))

        other_coords = set()
        for x in range(other.x1, other.x2 + 1):
            for y in range(other.y1, other.y2 + 1):
                other_coords.add((x, y))

        return len(self_coords & other_coords) > 0


data = open(filename).read()

bricks = []
name = "A"

for line in data.splitlines():
    coords = [int(x) for x in line.replace("~", ",").split(",")]
    bricks.append(Brick(name, *coords))
    name = chr(ord(name) + 1)

bricks = sorted(bricks, key=attrgetter("z1", "z2"))

for i, brick in enumerate(bricks):
    curr_z = 1
    for other in bricks[:i]:
        if other.supports(brick):
            curr_z = max(curr_z, other.z2 + 1)
    height = brick.z2 - brick.z1
    brick.z1 = curr_z
    brick.z2 = curr_z + height

supporting = defaultdict(set)
supported = defaultdict(set)

for i, brick in enumerate(bricks):
    for other in bricks[:i]:
        lower_z = max(other.z1, other.z2)
        upper_z = min(brick.z1, brick.z2)
        z_diff = upper_z - lower_z
        if other.supports(brick) and z_diff == 1:
            supporting[other].add(brick)
            supported[brick].add(other)

total = 0

for brick in bricks:
    queue = deque()
    fall = set([brick])

    for other in supporting[brick]:
        if len(supported[other]) == 1:
            queue.append(other)
            fall.add(other)

    while queue:
        brick = queue.popleft()

        for other in supporting[brick]:
            if other in fall:
                continue
            if supported[other].issubset(fall):
                queue.append(other)
                fall.add(other)

    total += len(fall) - 1

print(total)
