from collections import deque
n = int(input())
graph = [[0] * n for _ in range(n)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

direction = {}

for _ in range(int(input())):
    x, c = input().split()
    direction[int(x)] = c

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 3 => l: 0 / r: 1
# 1 => l: 3 / r: 2
# 2 => l: 1 / r: 0
# 0 => l: 2 / r: 3
def direc(curr, d):
    if curr == 3:
        return 0 if d == "L" else 1
    elif curr == 2:
        return 1 if d == "L" else 0
    elif curr == 1:
        return 3 if d == "L" else 2
    elif curr == 0:
        return 2 if d == "L" else 3

snake = deque()
snake.append([0, 0])
sec = 0
d = 3

while True:
    ny = snake[-1][0] + dy[d]
    nx = snake[-1][1] + dx[d]
    sec += 1

    if [ny, nx] in snake or ny < 0 or ny >= n or nx < 0 or nx >= n:
        break

    # 여기에서 if-else로 나눴는데 시간이 더 걸려서 그냥 원래 코드로 냅둠
    if graph[ny][nx] == 0:
        snake.popleft()
    elif graph[ny][nx] == 1:
        graph[ny][nx] = 0

    snake.append([ny, nx])

    if sec in direction:
        d = direc(d, direction[sec])

print(sec)

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# direction = 0
# if direction_order == "D":
#     direction = direction + 1 if direction < 3 else 0
# elif direction_order == "L":
#     direction = direction - 1 if direction > 0 else 3









