def solution(nums):
    answer = 0
    length = len(nums) / 2
    sets = list(set(nums))
    print(sets)
    print(len(sets))
    
    if length <= len(sets):
        answer = length
    else:
        answer = len(sets)
    return answer