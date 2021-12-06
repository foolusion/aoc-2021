fish_ages = [int(i) for i in input().split(',')]

age_buckets = {i: 0 for i in range(9)}
for f in fish_ages:
    age_buckets[f] += 1

for d in range(256):
    temp = {i: 0 for i in range(9)}
    print(age_buckets)
    for k, v in age_buckets.items():
        if k == 0:
            temp[6] += v
            temp[8] += v
            continue
        temp[k-1] += v
    print(temp)
    age_buckets = temp

total = 0
for v in age_buckets.values():
    total += v

print(total)