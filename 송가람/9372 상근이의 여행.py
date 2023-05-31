import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    board = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    chk = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        chk[start] = 1
        while q:
            node = q.popleft()
            for i in board[node]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    chk[i] = 1

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += (sum(chk) - 1)
            chk = [0] * (N+1)

    print(cnt)
