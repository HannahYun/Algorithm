def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(1, number+1): # i = 2
        num = 0
        for j in range(1, int(i ** (1/2)) + 1): # 1 ~ 2, j = 1
            if i % j == 0:
                if (i ** (1/2)) == j:
                    num += 1
                else:
                    num += 2
            if num > limit:
                num = power
                break
        arr.append(num)
    answer = sum(arr)
    return answer