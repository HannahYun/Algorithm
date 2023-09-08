from itertools import combinations
def solution(nums):
    answer = 0

    comb = list(combinations(nums, 3))
    # print(comb)
    
    for c in comb:
        s = sum(c)
        result = 0
        for i in range(2, s):
            if s % i == 0:
                result = 1
                break
        if result == 0:
            answer += 1

    return answer