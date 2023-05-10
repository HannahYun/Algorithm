import sys
n, m = map(int, sys.stdin.readline().split())

arr = [[] for i in range(n)]
visited = [False] * n
result = False

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# [[1], [0, 2], [1, 3], [2, 4], [3]]

def dfs(start, depth):
    global result
    # print(start, depth)
    if depth == 5:
        result = True
        return
    
    for i in range(len(arr[start])): # [1]
        if visited[arr[start][i]] == False:
            visited[arr[start][i]] = True
            dfs(arr[start][i], depth+1)
            visited[arr[start][i]] = False

for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)