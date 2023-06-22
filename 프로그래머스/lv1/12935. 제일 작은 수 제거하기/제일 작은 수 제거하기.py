def solution(arr):
    answer = []
    num = min(arr)
    if num in arr:
        arr.remove(num)
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    return answer