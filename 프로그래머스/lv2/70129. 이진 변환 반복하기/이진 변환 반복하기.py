def solution(s):
    answer = []
    num = 0 # 변환 횟수
    b = 0 # 0의 개수
    while len(s) != 1:
        num += 1
        cnt = s.count("1")
        b += s.count("0")
        s = str(bin(cnt))[2:]
    answer.append(num)
    answer.append(b)
    return answer
