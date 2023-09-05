def solution(n):
    ans = 0
    
    while True:
        if n % 2 == 0: # 짝수
            n /= 2
        else: # 홀수
            if n == 1:
                ans += 1
                return ans
            ans += 1
            n -= 1
            n /= 2

    return ans