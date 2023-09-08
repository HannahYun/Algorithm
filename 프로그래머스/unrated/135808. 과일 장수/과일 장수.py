def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)

    share = len(score) // m # 몫
    tmp = []
    for i in range(0, share*m):
        tmp.append(score[i])
        if len(tmp) == m:
            min_score = min(tmp)
            answer += min_score * m
            tmp = []
        # print(tmp)
    return answer