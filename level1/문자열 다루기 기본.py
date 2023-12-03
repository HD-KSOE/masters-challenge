def solution(s):
    answer = True
    
    s = list(str(s))
    l = len(s)
    
    if l == 4 or l == 6:
        for i in range(l):
            if ord(s[i]) >= 65:
                answer = False
    else:
        answer = False
    
    return answer