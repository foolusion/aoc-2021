height_map = []
with open("day_09.in") as f:
    for line in f:
        row = [int(i) for i in line.strip()]
        height_map.append(row)

total = 0
basin_points = []
for y, row in enumerate(height_map):
    for x, height in enumerate(row):
        if x > 0:
            if height_map[y][x - 1] <= height:
                continue
        if y > 0:
            if height_map[y - 1][x] <= height:
                continue
        if x < len(height_map[0]) - 1:
            if height_map[y][x + 1] <= height:
                continue
        if y < len(height_map) - 1:
            if height_map[y + 1][x] <= height:
                continue
        basin_points.append((x, y))
        total += height + 1

print(total)

basins = []
for b in basin_points:
    basin = []
    frontier = [b]
    seen = set()
    while frontier:
        f = frontier.pop()
        if f in seen:
            continue
        seen.add(f)
        if (
            f[0] < 0
            or f[0] >= len(height_map[0])
            or f[1] < 0
            or f[1] >= len(height_map)
        ):
            continue
        if height_map[f[1]][f[0]] == 9:
            continue
        basin.append(f)
        frontier += [
            (f[0] + 1, f[1]),
            (f[0] - 1, f[1]),
            (f[0], f[1] + 1),
            (f[0], f[1] - 1),
        ]
    basins.append(basin)

result = sorted(basins, key=len, reverse=True)
total = 1
for i in result[:3]:
    print(len(i))
    total *= len(i)
print(total)
