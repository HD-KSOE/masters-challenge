def solution(n):
    answer = 0
    
    x = n
    while x > 0:
        if n % x == 1:
            answer = x
        x -= 1
    
    return answer
