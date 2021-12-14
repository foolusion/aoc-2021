def count(foo, index):
    total = 0
    for p in foo:
        total += p[index]
    return total


power = [[int(i) for i in input()] for _ in range(1000)]

o = power
for i in range(len(o[0])):
    if len(o) == 1:
        break
    c = count(o, i)
    if c >= (len(o) / 2):
        o = [p for p in o if p[i] == 1]
    else:
        o = [p for p in o if p[i] == 0]
oxygen = int("".join(str(i) for i in o[0]), 2)

co2 = power
for i in range(len(co2[0])):
    if len(co2) == 1:
        break
    c = count(co2, i)
    if c < (len(co2) / 2):
        co2 = [p for p in co2 if p[i] == 1]
    else:
        co2 = [p for p in co2 if p[i] == 0]
carbon_dioxide = int("".join(str(i) for i in co2[0]), 2)

print(oxygen * carbon_dioxide)

# counts = [0 for _ in range(len(power[0]))]
# for p in power:
#     for index, digit in enumerate(p):
#         if digit == '1':
#             counts[index] += 1

# g = []
# e = []
# for x in counts:
#     if x > 500:
#         g.append('1')
#         e.append('0')
#     else:
#         g.append('0')
#         e.append('1')

# gamma = int(''.join(g), 2)
# epsilon = int(''.join(e), 2)

# print(gamma*epsilon)
