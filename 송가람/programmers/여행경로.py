import copy

def solution(tickets):
    
    answer = []
    tickets.sort()
    visited = [False] * (len(tickets))
            
    def dfs(start, depth, visited, answer):
        if depth == len(tickets) - 1:
            answer.append(start)
            return answer
        temp_v = copy.deepcopy(visited)
        temp_a = copy.deepcopy(answer)
        for idx in range(len(tickets)):
            if not visited[idx]:
                if tickets[idx][0] == start:
                    temp_a.append(tickets[idx][0])
                    temp_v[idx] = True
                    result = dfs(tickets[idx][1], depth+1, temp_v, temp_a)
                    if result:
                        return result
                    temp_v = copy.deepcopy(visited)
                    temp_a = copy.deepcopy(answer)
        
        
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            answer.append(tickets[i][0])
            visited[i] = True
            ans = dfs(tickets[i][1], 0, visited, answer)
            if ans:
                return ans
            answer = []
            visited = [False] * (len(tickets))


a = solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]])
print(a)