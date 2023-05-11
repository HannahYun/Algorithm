import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
com = list(itertools.combinations_with_replacement(arr, m))
com = list(set(com))
com.sort()

for i in range(len(com)):
    print(*com[i])