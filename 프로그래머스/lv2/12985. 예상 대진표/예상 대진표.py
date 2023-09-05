def solution(n,a,b):
    answer = 1
    n1, n2 = a, b
    while True:
        if (n1 + 1) // 2 == (n2 + 1) // 2 or (n2 + 1) // 2 == (n1 + 1) // 2:
            return answer
        else:
            answer += 1
            n1 = (n1 + 1) // 2
            n2 = (n2 + 1) // 2
        

    return answer