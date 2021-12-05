points = []
with open('day_05.in') as f:
    for line in f:
        p1, p2 = line.split('->')
        p1 = p1.strip()
        p2 = p2.strip()
        x1, y1 = [int(p) for p in p1.split(',')]
        x2, y2 = [int(p) for p in p2.split(',')]
        points.append(((x1, y1), (x2, y2)))

world = [[0 for x in range(1000)] for y in range(1000)]
for p in points:
    if p[0][0] == p[1][0]:
        y1 = min(p[0][1], p[1][1])
        y2 = max(p[0][1], p[1][1])
        for y in range(y1, y2+1):
            x = p[0][0]
            world[y][x] += 1
    elif p[0][1] == p[1][1]:
        x1 = min(p[0][0], p[1][0])
        x2 = max(p[0][0], p[1][0])
        for x in range(x1, x2 + 1):
            y = p[0][1]
            world[y][x] += 1
    else:
        t = p[0]
        dx = 1 if p[0][0] < p[1][0] else -1
        dy = 1 if p[0][1] < p[1][1] else -1
        while t != p[1]:
            world[t[1]][t[0]] += 1
            t = (t[0]+dx, t[1]+dy)
        world[t[1]][t[0]] += 1

total = 0
for row in world:
    for col in row:
        if col > 1:
            total += 1

print(total)
