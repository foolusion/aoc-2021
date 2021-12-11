chunk_lines = []
with open('day_10.in') as f:
    for line in f:
        chunk = [i for i in line.strip()]
        chunk_lines.append(chunk)

def match(o, c):
    return (o == '(' and c == ')') or (o == '[' and c == ']') or(o == '{' and c == '}') or (o == '<' and c == '>')
    

score = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0
for line in chunk_lines:
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
            continue
        o = stack.pop()
        if not match(o, c):
            total += score[c]
print(total)

def process_line(line):
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
            continue
        o = stack.pop()
        if not match(o, c):
            return None
    return stack
    

score = {'(': 1, '[': 2, '{': 3, '<': 4}
line_scores = []
for line in chunk_lines:
    stack = process_line(line)
    if stack is None:
        continue
    print(stack)
    total = 0
    while stack:
        o = stack.pop()
        total *= 5
        total += score[o]
    line_scores.append(total)

print(sorted(line_scores)[len(line_scores)//2])
