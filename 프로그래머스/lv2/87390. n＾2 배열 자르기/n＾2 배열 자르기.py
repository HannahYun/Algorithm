def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        # 2 -> 0, 2 -> 3
        # 3 -> 1, 0 -> 2
        # 8 -> 2, 2 -> 3
        a = i // n
        b = i % n
        num = max(a, b) + 1
        answer.append(num)
        
    return answer