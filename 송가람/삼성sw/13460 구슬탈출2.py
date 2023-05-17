from collections import deque
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

def move(x, y, xi, yi):
    while True:
        x += xi
        y += yi
        if board[x][y] == '#':
            x -= xi
            y -= yi
            return x, y
        elif board[x][y] == 'O':
            return x, y

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    cnt = 0
    q = deque()
    q.append((xr, yr, xb, yb))
    visited = []
    visited.append((xr, yr, xb, yb))

    while q:
        if cnt > 10:
            return -1
        
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if board[rx][ry] == 'O':
                return cnt
            
            for i in range(4):
                nrx, nry = move(rx, ry, dx[i], dy[i])
                nbx, nby = move(bx, by, dx[i], dy[i])

                if board[nbx][nby] == 'O':
                    continue
                
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) < abs(nbx - bx) + abs(nby - by):
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]
                
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby))
                
        cnt += 1
    return -1

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == "R":
            xr, yr = i, j
        elif board[i][j] == "B":
            xb, yb = i, j

print(bfs())


# 10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########

# 4 5
#####
#.BR#
##O##
#####

# 6 6
######
#...R#
###..#
#.OB##
##...#
######


