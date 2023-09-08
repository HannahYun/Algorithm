def solution(n):
    answer = 0
    for i in range(2, n+1):
        result = 0
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                result = 1
                break
        if result == 0:
            answer += 1
    return answer