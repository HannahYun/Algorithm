def solution(s):
    answer = ''
    S = s.lower()
    
    for i in range(len(S)):
        if S[i].isdigit() == False and (S[i-1] == " " or i==0):
            k = S[i].upper()
            S = S[:i] + k + S[i+1:]
    # print(S)
    answer = S
    return answer