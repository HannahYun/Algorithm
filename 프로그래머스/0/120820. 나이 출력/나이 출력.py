def solution(age):
    answer = 0
    
    if age <= 23:
        answer = 2022 - age + 1
    else:
        ag = age - 23
        answer = 2000 - ag
    return answer