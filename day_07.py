import statistics

positions = sorted(int(i) for i in input().split(','))

goal = statistics.median_low(positions)
total = 0
for p in positions:
    total += abs(p - goal)
print(total)

goal = sum(positions)//len(positions)
total = 0
for p in positions:
    total += sum(range(abs(p - goal)+1))
print(goal)
print(total)
