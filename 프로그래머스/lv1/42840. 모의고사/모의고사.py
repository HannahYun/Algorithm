def solution(answers):
    answer = []
    user1 = [1, 2, 3, 4, 5] # 5
    user2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    n = len(answers)
    ans1, ans2, ans3 = 0, 0, 0
    for i in range(n):
        if user1[i % 5] == answers[i]:
            ans1 += 1
        if user2[i % 8] == answers[i]:
            ans2 += 1
        if user3[i % 10] == answers[i]:
            ans3 += 1
    ma = max(ans1, ans2, ans3)
    if ans1 == ma:
        answer.append(1)
    if ans2 == ma:
        answer.append(2)
    if ans3 ==  ma:
        answer.append(3)
    return answer