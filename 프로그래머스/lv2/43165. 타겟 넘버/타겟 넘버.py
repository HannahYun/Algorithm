def solution(numbers, target):
    answer = 0
    
    def dfs(start, depth):
        nonlocal answer
        if depth == len(numbers):
            if start == target:
                answer += 1
            return answer
        else:
            dfs(start + numbers[depth], depth + 1)
            dfs(start - numbers[depth], depth + 1)
    
    dfs(0, 0)
    return answer