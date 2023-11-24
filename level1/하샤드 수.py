def solution(x):
    answer = True
    total = 0
    
    z = list(str(x))
    for i in z:
        total += int(i)
    
    if x % total == 0:
        return answer
    else:
        answer = False
    
    return answer