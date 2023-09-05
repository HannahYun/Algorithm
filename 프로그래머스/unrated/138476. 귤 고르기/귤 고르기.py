def solution(k, tangerine):
    answer = 0
    
    arr = {}
    for i in range(len(tangerine)):
        if tangerine[i] in arr:
            arr[tangerine[i]] += 1
        else:
            arr[tangerine[i]] = 1
    li = list(arr.values())
    li.sort(reverse=True)
    
    for i in li:
        answer += 1
        if i >= k:
            break
        else:
            k -= i
            continue
    
    return answer