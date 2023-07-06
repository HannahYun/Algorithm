def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com
        i, j, k = i-1, j-1, k-1
        arr = array[i:j+1]
        arr.sort()
        # print(arr)
        answer.append(arr[k])
    return answer