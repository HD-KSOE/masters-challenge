from itertools import combinations

def solution(number):
    answer = 0
    count = 0
    c = list(combinations(number, 3))
    
    for i in c:
        if sum(i) == 0:
            count += 1
    answer = count
    return answer
