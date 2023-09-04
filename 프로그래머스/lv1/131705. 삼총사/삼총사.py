import itertools
def solution(number):
    answer = 0
    
    arr = list(itertools.combinations(number, 3))
    for s in arr:
        if sum(s) == 0:
            answer += 1
    return answer