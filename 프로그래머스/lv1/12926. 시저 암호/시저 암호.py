def solution(s, n):
    answer = ''
    print(ord('a'), ord('z')) # 97 122
    print(ord('A'), ord('Z')) # 65 90
    
    for i in s:
        i2 = ord(i) + n
        if i == " ":
            answer += " "
            continue
        if 96 < ord(i) < 123:
            if 96 < i2 < 123:
                i = chr(i2)
            else:
                i = chr(i2 - 26)
        else:
            if 64 < i2 < 91:
                i = chr(i2)
            else:
                i = chr(i2 - 26)
        answer += i
    
    return answer