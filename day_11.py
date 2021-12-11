dumbo = [[int(i) for i in input()] for _ in range(10)]

def dumbo_string(d):
    s = ''
    for row in d:
        s += ''.join(str(i) for i in row)
        s += '\n'
    return s

total = 0
for step in range(1000):
    flashing = set()
    for y, row in enumerate(dumbo):
        for x, d in enumerate(row):
            dumbo[y][x] += 1
            if dumbo[y][x] > 9:
                flashing.add((x, y))
    flashed = set()
    while flashing:
        total += 1
        d = flashing.pop()
        flashed.add(d)
        x, y = d
        for dx in range(-1,2):
            for dy in range(-1, 2):
                xx = x+dx
                yy = y+dy
                if xx < 0 or xx >= len(dumbo[1]) or yy < 0 or yy >= len(dumbo):
                    continue
                if (xx, yy) in flashed or (xx, yy) in flashing:
                    continue
                dumbo[yy][xx] += 1
                if dumbo[yy][xx] > 9:
                    flashing.add((xx, yy))
    for x, y in flashed:
        dumbo[y][x] = 0
    if len(flashed) == 100:
        print(step+1)
        break
print(total)
