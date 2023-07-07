def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    
    for sen in s:
        cnt = 0
        o = ord(sen)
        while True:
            if cnt == index:
                answer += chr(o)
                break
            o += 1
            if o >= 123:
                o = o - 26
            if chr(o) in skip:
                continue
            cnt += 1
        # answer += chr(o)
    return answer