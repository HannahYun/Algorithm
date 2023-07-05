def solution(s):
    answer = []
    li = list(s)
    li.reverse()
    
    for i in range(len(li)):
        cnt = 0
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                answer.append(j - i)
                cnt += 1
                break
        if cnt == 0:
            answer.append(-1)
    answer.reverse()
    return answer