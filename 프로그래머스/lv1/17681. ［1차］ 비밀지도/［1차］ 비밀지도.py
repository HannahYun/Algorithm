def solution(n, arr1, arr2):
    answer = []
    ar1 = []
    ar2 = []
    for i in range(n):
        a = str(bin(arr1[i]))[2:]
        b = str(bin(arr2[i]))[2:]
        if len(a) != n:
            a = "0" * (n - len(a)) + a
        if len(b) != n:
            b = "0" * (n - len(b)) + b
        ar1.append(a)
        ar2.append(b)
    print(ar1)
    
    
    for i in range(n):
        result = ""
        for j in range(n):
            if ar1[i][j] == "0" and ar2[i][j] == "0":
                result += " "
            else:
                result += "#"
        answer.append(result)
    return answer