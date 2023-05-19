#라면 사기
#뒤에서부터 계산하면 되는거 아닌가?
from sys import stdin
n = int(stdin.readline())
arr = []
for i in range(n):
    a, b = list(map(int, stdin.readline().split()))
    arr.append([a, b])

#우선되는 정렬이 앞에!먼저! 입력되어야 함
arr.sort(key=lambda x : (x[1], x[0]))
st = 0
cnt = 0
for i in range(len(arr)):
    if arr[i][0] >= st:
        cnt += 1
        st = arr[i][1]
print(cnt)