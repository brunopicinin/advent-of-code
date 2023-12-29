import sympy

# filename = "sample.txt"
filename = "input.txt"

data = open(filename).read()

rpx, rpy, rpz, rvx, rvy, rvz = sympy.symbols("rpx rpy rpz rvx rvy rvz")
polys = []

for line in data.splitlines():
    px, py, pz, vx, vy, vz = map(int, line.replace("@", ",").split(","))
    polys.append((rpx - px) * (vy - rvy) - (rpy - py) * (vx - rvx))
    polys.append((rpy - py) * (vz - rvz) - (rpz - pz) * (vy - rvy))

solution = sympy.solve(polys)[0]

print(solution[rpx] + solution[rpy] + solution[rpz])
