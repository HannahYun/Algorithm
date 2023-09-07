def solution(want, number, discount):
    answer = 0
    length = sum(number)
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount)):
        dic2 = dic.copy()
        cnt = 0
        for j in range(i, i+10):
            if len(discount) - i < 10: # 14 - 4(!5) 까지 가능
                break
            if discount[j] in dic2 and dic2[discount[j]] != 0:
                dic2[discount[j]] -= 1
                cnt += 1
        if cnt == length:
            answer += 1
        
    return answer