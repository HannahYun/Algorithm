def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=lambda x : len(x))
    
    answer.append(int(s[0]))
    for i in range(len(s)-1):
        set_a = set(s[i].split(','))
        set_b = set(s[i+1].split(','))
        result = set_b - set_a
        answer.append(int(list(result)[0]))
    return answer