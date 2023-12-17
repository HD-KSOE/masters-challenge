def solution(s):
    result = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for j in s:
        if(j.isnumeric()): # 숫자는 그대로 
            result += j
        else: # 숫자가 아니라면, tmp에 이어붙임
            tmp += j
            if tmp in arr: # tmp를 계속 확인하면서 arr 안에 포함되어 있을 시 result에 숫자로 변환하여 추가
                result += str(arr.index(tmp))
                tmp = ""
    return int(result)
