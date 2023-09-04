def solution(s):
    answer = ''
    s = list(s)
    arr = []
    for i in s:
        arr.append(ord(i))
    arr.sort(reverse=True)
    
    for i in arr:
        answer += chr(i)
    
    return answer