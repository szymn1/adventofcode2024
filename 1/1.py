from operator import countOf


l1 = []
l2 = []
dist = 0
similarity_score = 0

with open('../input', 'r') as f:
    for line in f:
        line_content = line.split()
        l1.append(line_content[0])
        l2.append(line_content[1])

l1.sort()
l2.sort()
l1 = [int(i) for i in l1]
l2 = [int(i) for i in l2]


dist = sum([abs(i - j) for i, j in zip(l1, l2)])
print(f'Dist: {dist}')

similarity_score = sum([i * countOf(l2, i) for i in l1])

print(f'Similarity score: {similarity_score}')
