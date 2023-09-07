from collections import deque
def solution(cacheSize, cities):
    answer = 0
    arr = deque([])
    
    for city in cities:
        city = city.upper()
        if cacheSize == 0:
            answer += 5
            continue
        if city not in arr:
            if len(arr) < cacheSize:
                arr.append(city)
            else:
                arr.popleft()
                arr.append(city)
            answer += 5
        else:
            arr.remove(city)
            arr.append(city)
            answer += 1
    
    return answer