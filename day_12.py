adjacency = {}
with open("day_12.in") as f:
    for line in f:
        a, b = line.strip().split("-")
        adjacency[a] = adjacency.get(a, []) + [b]
        adjacency[b] = adjacency.get(b, []) + [a]

small_caves = set(cave for cave in adjacency.keys() if cave.islower())
paths = 0
states = [("start", {"start"}, False)]
while states:
    current, been, double_visit = states.pop()
    if current == "end":
        paths += 1
        continue
    for step in adjacency[current]:
        if step.islower():
            if step in been:
                if double_visit or step in ("start", "end"):
                    continue
                else:
                    states.append((step, been, True))
            else:
                states.append((step, been | {step}, double_visit))
        else:
            states.append((step, been, double_visit))
print(paths)
