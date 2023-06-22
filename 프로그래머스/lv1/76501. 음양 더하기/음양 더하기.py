def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        print(signs[i])
        if signs[i] == True:
            answer += absolutes[i]
        if signs[i] == False:
            answer -= absolutes[i]
        print(answer)
    return answer