import copy
n, m = map(int, input().split())
board = []
cctv = []
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mod = [
[],
[[0], [1], [2], [3]],
[[0, 1], [2, 3]],
[[0, 2], [1, 3], [0, 3], [1, 2]],
[[0, 2, 3], [2, 3, 1], [0, 1, 2], [0, 1, 3]],
[[0, 1, 2, 3]],
]


for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if line[j] in [1, 2, 3, 4, 5]:
            cctv.append([line[j], i, j])


def check(board, direction, x, y):
    for i in direction:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if n <= nx or 0 > nx or m <= ny or 0 > ny:
                break
            elif board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = '#'

def dfs(depth, board):
    global min_blind_spot
    # 마지막 시시티비까지 도착했을 때 사각지대 갯수 세기
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)
        min_blind_spot = min(min_blind_spot, count)
        return
    temp = copy.deepcopy(board)
    num, x, y = cctv[depth]
    for d in mod[num]:
        check(temp, d, x, y)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(board)



min_blind_spot = 65
dfs(0, board)
print(min_blind_spot)