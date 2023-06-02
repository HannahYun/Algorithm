import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# print(arr)

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 맨 왼쪽
            arr[i][j] += arr[i-1][j]
        elif j == i: # 맨 오른쪽
            arr[i][j] += arr[i-1][j-1]
        else: # 사잇값
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

# print(arr)
print(max(arr[n-1]))