def solution(n):
    answer = ''
    
    if n % 2 == 0: # 짝수라면
        answer = "수박" * (n // 2)
    else:
        answer = "수박" * (n // 2) + "수"
    return answer