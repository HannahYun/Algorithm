import math

def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(speeds))]
    print(day)
    
    cnt = 1
    max_day = day[0]
    for i in range(1, len(day)):
        if day[i] <= max_day:
            if i == len(day) - 1:
                cnt += 1
                answer.append(cnt)
                break
            else:
                cnt += 1
        else:
            if i == len(day) - 1:
                answer.append(cnt)
                answer.append(1)
                break
            answer.append(cnt)
            max_day = day[i]
            cnt = 1
    return answer