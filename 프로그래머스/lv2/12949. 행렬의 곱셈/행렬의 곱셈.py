import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    arr = np.dot(arr1, arr2)
    answer = arr.tolist()
    
    return answer