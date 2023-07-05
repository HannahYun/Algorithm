def solution(id_list, report, k):
    num_user = len(id_list)
    answer = [0] * num_user    
    result = [0] * num_user # 신고당한 횟수
    reports = [[] for i in range(num_user)] # 신고한 유저
    
    for i in range(len(report)):
        user, rep_user = report[i].split()
        idx = id_list.index(user)
        idz = id_list.index(rep_user)
        
        if rep_user not in reports[idx]:
            result[idz] += 1
            reports[idx].append(rep_user)
    
    for i in range(len(result)): # 신고당한 횟수
        if result[i] >= k:
            user = id_list[i]
            for j in range(num_user):
                if user in reports[j]:
                    answer[j] += 1
    return answer