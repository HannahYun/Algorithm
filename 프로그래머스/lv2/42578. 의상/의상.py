import itertools

def solution(clothes):
    dic = {}
    length = len(clothes)
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
    
    result = 1
    for i in dic:
        result *= len(dic[i]) + 1
    
    result -= 1
    
    return result