import sys
n = int(sys.stdin.readline())

answer = 0
for i in range(1, n):
    answer += n * i + i

print(answer)