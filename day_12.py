adjacency = {}
with open('day_12.in') as f:
	for line in f:
		a, b = line.strip().split('-')
		adjacency[a] = adjacency.get(a, []) + [b]
		adjacency[b] = adjacency.get(b, []) + [a]

small_caves = set(cave for cave in adjacency.keys() if cave.islower())
paths = []
states = [('start', {'start'}, ['start'], False)]
while states:
	current, been, path, double_visit = states.pop()
	print(f'Step: current={current}, been={been}, path={path}, double_visit={double_visit}')
	if current == 'end':
		paths.append(path)
		continue
	for step in adjacency[current]:
		if step.islower():
			if step in been:
				if double_visit:
					continue
				elif step in ('start', 'end'):
					continue
				else:
					states.append((step, been, path + [step], True))
			else:
				states.append((step, been | {step}, path + [step], double_visit))
		else:
			states.append((step, been, path + [step], double_visit))
print(len(paths))
