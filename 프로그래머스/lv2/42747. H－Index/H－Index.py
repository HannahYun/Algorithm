def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(len(citations), 0, -1): #54321
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i:
            answer = i
            break
    return answer