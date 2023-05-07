import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
li = list(sys.stdin.readline().split())
li.sort()

result = []
for i in list(combinations(li, l)):
    new = [*i]
    mo = ["a", "e", "i", "o", "u"]
    new.sort()
    count_m, count_n = 0, 0
    for n in new:
        if n in mo:
            count_m += 1
        else:
            count_n += 1
    if new not in result and count_m >= 1 and count_n >= 2: # aeiou 한개 이상 포함
        result.append(new)

# 결과 출력
for r in result:
    print("".join(r))