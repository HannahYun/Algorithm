def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i == 1:
            answer -= 1
            continue
        cnt = 2 # 약수의 개수(1, 자기자신 포함)
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer