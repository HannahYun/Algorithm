def solution(players, callings):
    answer = []
    dic1 = {}
    dic2 = {}
    for i in range(len(players)):
        dic1[players[i]] = i
        dic2[i] = players[i]
    
    for c in callings:
        present = dic1[c] # 현재 랭크
        n = dic2[present-1]
        dic2[present-1], dic2[present] = dic2[present], dic2[present-1]
        dic1[n] += 1
        dic1[c] -= 1
    answer = list(dic2.values())
    return answer