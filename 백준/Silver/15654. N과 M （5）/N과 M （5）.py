import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
com = list(itertools.permutations(arr, m))

for i in range(len(com)):
    print(*com[i])