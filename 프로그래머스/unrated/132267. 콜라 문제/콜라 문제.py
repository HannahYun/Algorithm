def solution(a, b, n):
    answer = 0
    cnt = 0
    
    while True:
        if n < a:
            break
        else:
            k = n % a # 나머지
            k2 = (n // a) * b
            answer += k2
            n = k2 + k
    return answer