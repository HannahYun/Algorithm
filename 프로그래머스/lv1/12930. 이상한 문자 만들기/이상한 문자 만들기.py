def solution(s):
    answer = ''
    num = 0
    for i in s:
        if i == " ":
            num = 0
            answer += " "
            continue
        else:
            if num % 2 == 0:
                answer += i.upper()
                num += 1
            else:
                answer += i.lower()
                num += 1
    return answer