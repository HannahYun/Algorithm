def solution(n):
    answer = 0
    arr = [0] * n
    
    def dfs(depth):
        nonlocal answer
        if depth == n:
            answer += 1
            return 1
        for j in range(1, n+1): # 현재 행의 값
            arr[depth] = j
            if depth == 0:
                dfs(depth+1)
                continue
            for l in range(0, depth): # 현재보다 이전 인덱스(행)들
                if arr[l] == j or depth - l == abs(arr[l] - j):
                    break
                if l == depth -1:
                    dfs(depth+1)

    dfs(0)
    return answer