def solution(phone_number):
    answer = ''
    l = len(phone_number)
    phone_number = list(str(phone_number))
    
    for i in range(0, l-4, 1):
        phone_number[i] = "*"
    answer = ''.join(phone_number)
        
    return answer