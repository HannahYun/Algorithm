def solution(t, p):
    answer = 0
    lp = len(p)
    
    for i in range(0, len(t)-lp+1):
        result = ""
        for j in range(i, i+lp):
            result += t[j]
        if int(result) <= int(p):
            answer += 1
    return answer