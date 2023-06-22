def solution(phone_number):
    answer = ''
    arr = list(phone_number)
    num = len(arr)
    arr[:-4] = "*" * (num - 4)
    arr2 = arr[:-4] + arr[-4:]
    
    arr2 = ''.join(arr2)
    print(arr2)
    return arr2