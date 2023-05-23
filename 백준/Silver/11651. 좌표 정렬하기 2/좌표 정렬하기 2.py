n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

# print(arr)
arr.sort(key= lambda arr: (arr[1], arr[0]))

for x, y in arr:
    print(x, y)