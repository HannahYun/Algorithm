# 11053
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 10 20 15 18 7 25 10 50 => 5
# 20 10 15 18 30 => 4

li = [1 for i in range(n)]
for i in range(1, n): # 현재 위치
    for j in range(i): # 앞 부분
        if a[i] > a[j]:
            if li[j] >= li[i]:
                li[i] = li[j] + 1
    # print(li)
print(max(li))