import sys
n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(n, m+1):
    if i == 1: #1은 소수아님
        continue
    for j in range(2, int(i**0.5) +1):
        if i % j == 0:
            break
    else:
        arr.append(i)

for i in arr:
    print(i)