dots = []
folds = []
with open("day_13.in") as f:
    reading_dots = True
    for line in f:
        if line == "\n":
            reading_dots = False
            continue
        if reading_dots:
            x, y = [int(i) for i in line.strip().split(",")]
            dots.append((x, y))
        else:
            fold_str = line.strip().split(" ")
            a, b = fold_str[2].split("=")
            folds.append((a, int(b)))

for dir, pos in folds:
    for i, (x, y) in enumerate(dots):
        if dir == "y" and y > pos:
            dots[i] = (x, pos - (y - pos))
        if dir == "x" and x > pos:
            dots[i] = (pos - (x - pos), y)
    dots = list(set(dots))

x_max = max(dots, key=lambda x: x[0])[0]
y_max = max(dots, key=lambda x: x[1])[1]
mat = [["." for j in range(x_max + 1)] for i in range(y_max + 1)]
for x, y in dots:
    mat[y][x] = "#"
for row in mat:
    print("".join(row))
