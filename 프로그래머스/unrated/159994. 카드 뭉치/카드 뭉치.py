def solution(cards1, cards2, goal):
    answer = ''
    for g in goal:
        if len(cards1) != 0 and g in cards1[0]:
            cards1.pop(0)
        elif len(cards2) != 0 and g in cards2[0]:
            cards2.pop(0)
        else:
            answer = "No"
            break
    if answer != "No":
        answer = "Yes"
    return answer