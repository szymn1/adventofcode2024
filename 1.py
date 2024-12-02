l1 = []
l2 = []
dist = 0

with open('input', 'r') as f:
    for line in f:
        line_content = line.split()
        l1.append(line_content[0])
        l2.append(line_content[1])

l1.sort()
l2.sort()

dist = sum([abs(int(i) - int(j)) for i, j in zip(l1, l2)])
print(dist)
