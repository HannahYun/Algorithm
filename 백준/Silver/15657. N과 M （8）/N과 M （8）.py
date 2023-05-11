import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
com = list(itertools.combinations_with_replacement(arr, m))

for i in range(len(com)):
    print(*com[i])