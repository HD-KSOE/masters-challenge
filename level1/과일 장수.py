def solution(k, m, score):
    answer = 0
    score.sort() # 1 1 2 2 2 2 4 4 4 4 4 4
    print(score)
    temp = []
    for i in range(len(score) // m):
        for j in range(m):        
            temp.append(score[len(score)-1-(m*i)-j])
        answer += min(temp) * m  
        
        print(answer)
    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
print(solution(k, m, score))