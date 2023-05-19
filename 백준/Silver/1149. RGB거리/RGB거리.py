import sys

n = int(sys.stdin.readline())
house = [0] * (n)

for i in range(n):
    house[i] = list(map(int, sys.stdin.readline().split()))
    
# 이전 값의 최솟값과 자기 자신 더한 값으로 업데이트 => 최소 비용
for i in range(1, n):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[-1][0], house[-1][1], house[-1][2]))