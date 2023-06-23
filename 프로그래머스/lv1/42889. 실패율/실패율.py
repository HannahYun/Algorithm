def solution(N, stages):
    answer = []
    go = [0 for i in range(N+1)] # 도달 수
    n_clear = [0 for i in range(N+1)] # 클리어 X
    fail = {} # 실패율
    
    for i in stages:
        n_clear[i-1] += 1
        for j in range(i):
            go[j] += 1
            
    # print(go)
    # print(n_clear)
    for i in range(N):
        if go[i] != 0:
            fail[i+1] = n_clear[i] / go[i] # 실패율
        else:
            fail[i+1] = 0
    # print(fail)
    
    answer = sorted(fail, key=lambda x:fail[x], reverse=True)
    # print(answer)
    return answer