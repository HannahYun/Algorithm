def solution(s):
    answer = 0
    length = len(s)
    
    cnt1 = 0
    cnt2 = 0
    start = True
    idx = 0
    for i in range(length):
        if start:
            cnt1 += 1
            idx = i
            start = False
        else:
            if s[idx] == s[i]:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == cnt2 or i == length - 1:
            start = True
            cnt1 = 0
            cnt2 = 0
            answer += 1
    return answer