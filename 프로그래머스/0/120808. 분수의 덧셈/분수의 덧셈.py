import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    print(numer, denom)
    
    if denom == numer:
        answer = [1, 1]
    elif denom > numer:
        for i in range (numer, 0, -1):
            if denom % i == 0 and numer % i == 0:
                answer = [numer // i, denom // i]
                break
            answer = [numer, denom]
    else:
        for i in range(denom, 0, -1):
            if denom % i == 0 and numer % i == 0:
                answer = [numer // i, denom // i]
                break
            answer = [numer, denom]
    return answer