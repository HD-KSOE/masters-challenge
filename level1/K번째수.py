def solution(array, commands):
    answer = []
    tmp = []
    for i in range(len(commands)):
        for j in range(commands[i][0], commands[i][1] + 1):
            tmp.append(array[j-1])
        
        tmp.sort()
        
        answer.append(tmp[commands[i][2]-1])
        tmp = []

    return answer
