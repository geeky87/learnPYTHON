from collections import Counter
from sortedcontainers import sortedlist

c = Counter("Hello this is my first Counter")

print(c)
print(sorted(c))

print(c.most_common(1))

a = [1, 3, 1, 4, 2, 3, 5, 4]
k = sortedlist[a]
print(k)
