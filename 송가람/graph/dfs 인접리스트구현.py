n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, i, visited):
  visited[i] = True
  print(i, end=' ')
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)

dfs(graph, 1, visited)

print(graph)

# 인접행렬
# n, m, v = map(int, input().split())
# matrix = [[0] * (n+1) for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#   f, t = map(int, input().split())
#   matrix[f][t] = matrix[t][f] = 1

# def dfs(matrix, i, visited):
#   visited[i] = True
#   print(i, end=' ')
#   for c in range(len(matrix[i])):
#     if matrix[i][c] == 1 and not visited[c]:
#       dfs(matrix, c, visited)
# dfs(matrix, v, visited)