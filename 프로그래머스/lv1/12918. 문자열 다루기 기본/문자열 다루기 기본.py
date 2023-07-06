def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    for i in s:
        if i.isdigit() == True:
            continue
        else:
            answer = False
    return answer