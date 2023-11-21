def solution(players, callings):
    answer = []
    dict = {}
    i = 0
    for i in range(len(players)):
        dict[players[i]] = i
    
    for calling in callings:
        index = dict[calling] 
        dict[calling] -= 1 
        dict[players[index-1]] += 1 
        players[index], players[index-1] = players[index-1], players[index]
    
    answer = players
    return answer
