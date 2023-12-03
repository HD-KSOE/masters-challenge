def solution(n):
    answer = 0
    
    num = n**(1/2)
    if num - int(num) == 0:
        answer = int((int(num) + 1)**2)
    else:
        answer = -1
    
    return answer