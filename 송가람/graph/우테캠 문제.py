import copy

def solution(n, network, repair):
    graph = [[] for _ in range(n+1)]

    for l in network:
        graph[l[0]].append(l[1])
        graph[l[1]].append(l[0])

    def dfs(graph, node, visited, cnt):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                cnt += 1
                cnt = dfs(graph, i, visited, cnt)
        
        return cnt
    
    min_price = 100001
    # repair 시도
    for r in repair:
        visited = [False] * (n + 1)
        repaired = copy.deepcopy(graph)
        repaired[r[0]].append(r[1])
        repaired[r[1]].append(r[0])
        linked = dfs(repaired, network[0][0], visited, 0)
        if linked + 1 == n:
            if min_price > r[2]:
                min_price = r[2]
    
    if min_price == 100001:
        return -1
    else:
        return min_price

# test case
# n = 6
# network = [[1, 2], [3, 5], [4, 2], [5, 6]]
# repair = [[3, 2, 10], [5, 4, 15]]
print(solution(4, [[1, 2]], [[3, 4, 10], [3, 2, 12]]))
