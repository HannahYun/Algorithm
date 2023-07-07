def solution(n, m):
    answer = []
    mi = min(n, m)
    a, b, c = 0, 0, 0
    for i in range(1, mi+1):
        if n % i == 0 and m % i == 0:
            a = i
            b = n // i
            c = m // i
    answer.append(a)
    answer.append(a*b*c)
    return answer