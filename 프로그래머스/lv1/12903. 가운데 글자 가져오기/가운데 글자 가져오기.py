def solution(s):
    answer = ''
    le = len(s) // 2 # 몫
    if len(s) % 2 == 0: # 짝수
        answer += s[le-1]
        answer += s[le]
    else: # 홀수
        answer += s[le]
    return answer