def solution(s):
    answer = -1
    arr = [s[0]]
    for i in range(1, len(s)):
        if len(arr) != 0 and arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])

    if len(arr) == 0:
        answer = 1
    else:
        answer = 0

    return answer