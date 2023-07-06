def solution(sizes):
    answer = 0
    si1 = []
    si2 = []
    for s in sizes:
        s.sort()
        si1.append(s[0])
        si2.append(s[1])
    si1.sort()
    si2.sort()
    answer = si1[-1] * si2[-1]
    print(si1)
    return answer