def solution(n):
    answer = 0
    for i in range(1, n+1): # 시작 숫자
        cnt = 0
        if i == n:
            answer += 1
            break
        for j in range(i, n+1): # 끝나는 숫자
            cnt += j
            if cnt == n:
                answer += 1
                break
            if cnt > n:
                break
    return answer