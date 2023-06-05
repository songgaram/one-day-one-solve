import sys
from collections import deque
import math
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(len(arr)):
    graph[i+1].append(arr[i])

print(graph)

def bfs(start, cnt):
    q = deque()
    q.append([start, cnt])
    visited[start] = True
    while q:
        node, c = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append([i, c+1])
                visited[i] = True
    
    return c

ans = []
for j in arr:
    if not visited[j]:
        a = bfs(j, 1)
        ans.append(a)
answer = 0
for l in ans:
    answer += math.comb(l, 2)
print(answer)
