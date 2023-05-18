from collections import deque
import sys

n = int(sys.stdin.readline())
arr = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
    
queue = deque()
queue.append(1) # 트리의 root = 1

result = [0]*(n+1) # 부모 노드
def bfs():
    while queue:
        que = queue.popleft()
        for q in arr[que]:
            if result[q] == 0:
                result[q] = que # 부모 노드로 변경
                queue.append(q)
                
bfs()
for i in range(2, n+1):
    print(result[i])