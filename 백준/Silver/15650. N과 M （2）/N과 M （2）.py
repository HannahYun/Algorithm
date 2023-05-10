import itertools

n, m = map(int, input().split())
arr = [str(i) for i in range(1, n+1)]
com = list(itertools.combinations(arr, m))

for i in range(len(com)):
    print(*com[i])