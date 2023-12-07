def sol(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def solution(n):
    answer = 0
    tmp = sol(n, 3)
    tmp2 = str(tmp)[::-1]
    answer = int(tmp2, 3)
    
    return answer
