def solution(name, yearning, photo):
    answer = []
    ny = {}
    for i in range(len(name)):
        ny[name[i]] = yearning[i]
    
    for arr in photo:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] in ny:
                cnt += ny[arr[i]]
        answer.append(cnt)
    return answer