# 골드바흐의 추측
# 2 3 5 7 11 13

import sys

# 에라토스의 체 - 소수 구하기
check = [1] * 1000001
check[0] = 0
check[1] = 0
for i in range(2, int(1000001**0.5)+1):
    if check[i] == 1:
        for j in range(i**2, 1000001, i):
            check[j] = 0

while (True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in range(3, n, 2):
        if check[i] == 1 and check[n-i] == 1:
            print(n, "=", i, "+", n-i)
            cnt += 1
            break
    if cnt == 0:
        print("Goldbach's conjecture is wrong.")
    