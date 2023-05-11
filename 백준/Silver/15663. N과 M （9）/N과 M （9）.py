import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
com = list(itertools.permutations(arr, m))
com = list(set(com))
com.sort()

for i in range(len(com)):
    print(*com[i])