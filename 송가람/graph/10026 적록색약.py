import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dic1 = {
    'R' : 0,
    'G' : 0,
    'B' : 0,
}

dic2 = {
    'R' : 0,
    'B' : 0,
}

def dfs(x, y):
    c = board[x][y]
    
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == c:
                dfs(nx, ny)

    return

def dfs(x, y):
    c = board[x][y]
    
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 'R':
                dfs(nx, ny)

    return

visited = [[False] * n  for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dic1[board[i][j]] += 1
            dfs(i, j)

visited = [[False] * n  for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dic2[board[i][j]] += 1
            dfs(i, j)

# r, g, b  = list(dic.values())
# c = max(r, g) + b       
# s = sum(dic.values())
# print(s, c)
# print(dic)
