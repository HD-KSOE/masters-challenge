def solution(arr):
    answer = []
    
    arr_min = min(arr)
    idx = arr.index(arr_min)
    del arr[idx]
    
    if len(arr) == 0:
        arr.append(-1)
    
    answer = arr
    return answer