def solution(arr):
    answer = []
    tmp = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            tmp.append(arr[i])
    
    answer = tmp
    return answer