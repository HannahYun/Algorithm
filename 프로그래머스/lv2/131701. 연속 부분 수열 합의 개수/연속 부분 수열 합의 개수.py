def solution(elements):
    answer = 0
    li = []
    arr = elements + elements
    for i in range(1, len(elements)+1): # 길이
        s = 0
        for j in range(len(elements)):
            li.append(sum(arr[j:j+i]))
    li = set(li)
    answer = len(li)
                
    return answer