def solution(n):
    answer = 0
    result = ''
    while (n>=3):
        result += str(n % 3)
        n = n // 3
    result += str(n)
    answer = int(result, 3)
    return answer