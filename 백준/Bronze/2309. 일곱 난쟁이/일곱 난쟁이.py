import sys
from itertools import combinations
n = []
for i in range(9):
    n.append(int(sys.stdin.readline()))
    
result = []
for i in list(combinations(n, 7)):
    if sum(i) == 100:
        result = [*i]
        break

result.sort()
for i in result:
    print(i)