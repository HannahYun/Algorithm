def solution(dartResult):
    answer = 0
    dig = []
    st = []
    l = 0
    for d in dartResult:
        if d.isdigit():
            if l == 1:
                dig[-1] = 10
                continue
            else:
                dig.append(int(d))
                l = 1
        else:
            l = 0
            st.append(d)
    
    n = 0
    for i in range(len(st)):
        if st[i] == "S" or st[i] == "D" or st[i] == "T":
            if st[i] == "S":
                dig[n] = dig[n] ** 1
            elif st[i] == "D":
                dig[n] = dig[n] ** 2
            elif st[i] == "T":
                dig[n] = dig[n] ** 3
            # print(dig)
            if i < len(st) -1:
                if (st[i+1] == "*" or st[i+1] == "#"):
                    continue
                else:
                    n += 1
                    continue
            else:
                n += 1
                continue
        
        if st[i] == "*":
            if i == 1:
                dig[n] = dig[n] * 2
            else:
                dig[n] = dig[n] * 2
                dig[n-1] = dig[n-1] * 2
            n += 1
        elif st[i] == "#":
            dig[n] = -dig[n]
            n += 1
        # print(dig)
    answer = sum(dig)
    return answer