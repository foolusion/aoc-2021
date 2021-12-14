import functools

start = ""
substitutions = {}
with open("day_14.in") as f:
    start = f.readline().strip()
    f.readline()
    for line in f:
        a, b = line.strip().split(" -> ")
        substitutions[a] = b

cur = start
for steps in range(10):
    temp = ""
    for i in range(len(cur)):
        pair = cur[i : i + 2]
        temp += cur[i] + substitutions.get(pair, "")
    cur = temp


frequencies = {}
for char in cur:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

x = max(frequencies.items(), key=lambda x: x[1])
y = min(frequencies.items(), key=lambda x: x[1])
print(f"max: {x} min: {y} {x[1]-y[1]}")


@functools.cache
def frequency(seq, depth):
    if depth == 0:
        freqs = {}
        for char in seq:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
        return freqs
    freqs = {}
    last = ""
    for pair in (seq[i : i + 2] for i in range(len(seq) - 1)):
        last = pair
        first = pair[0] + substitutions[pair] + pair[1]
        pair_freqs = frequency(first, depth - 1).copy()
        pair_freqs[pair[1]] -= 1
        for k, v in pair_freqs.items():
            if k in freqs:
                freqs[k] += v
            else:
                freqs[k] = v
    freqs[last[1]] += 1
    return freqs


frequencies = frequency(start, 40)
x = max(frequencies.items(), key=lambda x: x[1])
y = min(frequencies.items(), key=lambda x: x[1])
print(f"max: {x} min: {y} {x[1]-y[1]}")
