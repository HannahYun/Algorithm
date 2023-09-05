def solution(k, score):
    answer = []
    result = []
    
    for i in range(len(score)):
        if i < k:
            answer.append(score[i])
            answer.sort()
            result.append(answer[0])
        else:
            if score[i] >= answer[0]:
                answer[0] = score[i]
                answer.sort()
                result.append(answer[0])
            else:
                result.append(answer[0])
    return result