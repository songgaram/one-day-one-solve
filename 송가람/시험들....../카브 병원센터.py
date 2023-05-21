from collections import deque
def cal_min_time(n, node_from, node_to, level):
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    save = []
    for i in range(len(node_from)):
        a, b = node_from[i], node_to[i]
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    
    def bfs():
        while q:
            node, t = q.popleft()
            for i in graph[node]:       
                if not visited[i]:
                    if not save:
                        return t
                    if level[i-1] == 1:
                        save.remove(i)
                    q.append([i, t+1])
                    visited[i] = True
        return t

    for j in range(len(level)):
        if level[j] == 3:
            q.append([j+1, 1])
            # 3은 순서대로 넣고 visited 처리해줘서 더 가까운 3이 있으면 걔로 탐색을 돌기 때문에 먼 3이 탐색을 가지 않는다.
            visited[j+1] = True
        elif level[j] == 1:
            save.append(j+1)
    

    bfs()

  


cal_min_time(7, [1, 1, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3,1,3,2,2,2,1])
# print(cal_min_time(6, [1, 1, 1, 2, 3, 3, 5, 4], [2, 4, 3, 4, 4, 5, 6, 6], [3, 2, 3, 1, 2, 1]))