def solution(s):
    answer = ''
    s = list(s)
    l = len(s)
    if l % 2 == 0: # 짝수 길이
        answer = s[l//2 - 1] + s[l//2]
        print(answer)
    else:
        answer = s[int(l//2)]
    
    return answer