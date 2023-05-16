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
# print(solution(4, [[1, 2]], [[3, 4, 10], [3, 2, 12]]))

# Kruskal Algorithm
def solution(n, network, repair):

    def find_p(x):
        while x != parents[x]:
            x = parents[x]
        return x
    
    parents = [x for x in range(n + 1)]
    # sorted는 병합정렬을 기반으로 만들어져 O(nlog(n))
    repair.sort(key=lambda x: x[2])
    # network 가중치 0으로 넣어주기
    for i in range(len(network)):
        network[i].append(0)
    # repair/network 합치기
    edges = network + repair
    
    distance, cnt = 0, 0
    for a, b, value in edges:
        if find_p(a) != find_p(b):
            parents[find_p(b)] = find_p(a)
            distance += value
            cnt += 1
        
    if cnt == n - 1:
        return distance
    else:
        -1
print(solution(6, [[1, 2], [3, 5], [4, 2], [5, 6]], [[3, 2, 10], [5, 4, 15]]))