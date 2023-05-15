import sys
from collections import deque

# m: 가로, n: 세로
m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우

# 1. 시작부터 모든 토마토가 익어있는 경우 = 0
# 1이 있으면 큐에 삽입
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

# print(queue)
# bfs
while queue:
    x, y = queue.popleft()
    for i in range(4):
        x2, y2 = dx[i] + x, dy[i] + y
        if (0 <= x2 < n) and (0 <= y2 < m) and arr[x2][y2] == 0 and arr[x2][y2] != -1:
            arr[x2][y2] = arr[x][y] + 1
            queue.append([x2, y2])

# print(arr)
result = -1
# 2. 모두 익지 못하는 상황인 경우 = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result = 0

# 3. 모두 익을 때까지 최소 날짜 = day
if result == 0:
    print(-1)
else:
    day = max(map(max, arr))
    print(day - 1)