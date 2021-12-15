import sys

tile = []
with open("day_15.in") as f:
    for line in f:
        row = [int(i) for i in line.strip()]
        tile.append(row)

tw = len(tile[0])
th = len(tile)

grid = [[0 for j in range(tw * 5)] for i in range(th * 5)]
for i in range(th * 5):
    for j in range(tw * 5):
        ii = i // th
        jj = j // tw
        y = i % th
        x = j % tw
        grid[i][j] = tile[y][x] + ii + jj
        if grid[i][j] > 9:
            grid[i][j] -= 9

start = (0, 0)
goal = (len(grid[0]) - 1, len(grid) - 1)
cost = {(0, 0): 0}
state = [start]
visited = set()
while state:
    cur = state.pop(0)
    if cur in visited:
        continue
    visited.add(cur)
    c = cost[cur]
    if cur == goal:
        break
    if cur[0] > 0:
        left = (cur[0] - 1, cur[1])
        cc = min(cost.get(left, sys.maxsize), c + grid[left[1]][left[0]])
        cost[left] = cc
        state.append(left)
    if cur[0] < len(grid[0]) - 1:
        right = (cur[0] + 1, cur[1])
        cc = min(cost.get(right, sys.maxsize), grid[right[1]][right[0]] + c)
        cost[right] = cc
        state.append(right)
    if cur[1] > 0:
        up = (cur[0], cur[1] - 1)
        cc = min(cost.get(up, sys.maxsize), grid[up[1]][up[0]] + c)
        cost[up] = cc
        state.append(up)
    if cur[1] < len(grid) - 1:
        down = (cur[0], cur[1] + 1)
        cc = min(cost.get(down, sys.maxsize), grid[down[1]][down[0]] + c)
        cost[down] = cc
        state.append(down)
    state = sorted(state, key=lambda x: cost[x])

print(cost[goal])
