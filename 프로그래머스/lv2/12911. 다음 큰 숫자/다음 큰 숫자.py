def solution(n):
    answer = 0
    s = bin(n)[2:]
    a = s.count("1")
    
    for i in range(n+1, 1000001):
        t = bin(i)[2:]
        if t.count("1") == a:
            answer = int(t, 2)
            break
    return answer