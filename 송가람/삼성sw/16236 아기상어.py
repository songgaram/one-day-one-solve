import heapq
from collections import deque

field = []
n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    field.append(data)
    for j in range(n):
        if data[j] == 9:
            field[i][j] = 0
            sx, sy = i, j


def bfs(x, y):
    global visited
    size = 2
    fish = []
    distance = 0
    eat = 0
    q = deque()
    q.append([distance, x, y])
    visited[x][y] = True
    while True:
        while q:
            d, sx, sy = q.popleft()
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    # 물고기랑 상어랑 크기가 같은 경우 또는 물고기가 없는(0) 경우
                    if size == field[nx][ny] or field[nx][ny] == 0:
                        q.append([d + 1, nx, ny])
                        visited[nx][ny] = True
                    # 상어가 더 큰 경우
                    elif size > field[nx][ny]:
                        # 먹을 수 있는 물고기 힙에 넣기
                        heapq.heappush(fish, [d + 1, nx, ny])
                        visited[nx][ny] = True
        # 먹을 수 있는 물고기가 있다면
        if fish:
            fd, fx, fy = heapq.heappop(fish)
            q.append([0, fx, fy])
            distance += fd
            eat += 1
            # 초기화
            field[fx][fy] = 0
            visited = [[False] * n for _ in range(n)]
            visited[fx][fy] = True
            fish = []
        # 없으면 끝냄
        else:
            print(distance)
            return
        if eat == size:
            size += 1
            eat = 0


bfs(sx, sy)

