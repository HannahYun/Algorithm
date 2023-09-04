def solution(n, words):
    num, cnt = 0, 0

    for i in range(1, len(words)):
        
        if words[i-1][-1] != words[i][0] or (words[i] in words[:i-1]):
            num = i % n + 1
            cnt = i // n + 1
            break
            
    answer = [num, cnt] # 번호, 차례
    return answer