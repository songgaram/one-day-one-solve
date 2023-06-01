def solution(players, callings):
    dic = dict()
    for i in range(len(players)):
        dic[players[i]] = i
    
    for c in callings:
        temp = dic[c]
        dic[c] -= 1
        dic[players[temp - 1]] += 1
        players[temp] = players[temp - 1]
        players[temp - 1] = c
    
    return players