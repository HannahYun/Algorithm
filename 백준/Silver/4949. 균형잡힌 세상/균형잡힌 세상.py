import sys

while True:
    result = []
    fin = 0
    sen = sys.stdin.readline().rstrip()
    if sen == ".":
        break
    for s in sen:
        if s == ".":
            fin = 1
            break
        if s == "(" or s == "[":
            result.append(s)
        elif s == ")":
            if len(result) != 0 and result[-1] == "(":
                result.pop()
            else:
                break
        elif s == "]":
            if len(result) != 0 and result[-1] == "[":
                result.pop()
            else:
                break
    if len(result) == 0 and fin == 1:
        print("yes")
    else:
        print("no")
