def solution(a, b):
    answer = ''
    arr = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 일
    
    cnt = 0
    for i in range(1, a+1):
        if i == a:
            cnt += b
        else:
            cnt += day[i]
    answer = arr[cnt % 7]
    return answer