from sys import stdin
input = stdin.readline
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate(i, j, n, m):
    left_top = board[i][j]
    left_bottom = board[n-1][j]
    right_bottom = board[n-1][m-1]
    right_top = board[i][m-1]
    # left top
    for lt in range(n-1, i, -1):
        board[lt][i] = board[lt-1][i]
    # left_bottom
    for lb in range(m-1, i, -1):
        board[n-1][lb] = board[n-1][lb-1]
    # right_bottom
    for rb in range(i, n-1):
        board[rb][m-1] = board[rb+1][m-1]
    # right_top
    for rt in range(i, m-1):
        board[i][rt] = board[i][rt+1]
    board[i+1][j] = left_top
    board[n-1][j+1] = left_bottom
    board[n-2][m-1] = right_bottom
    board[i][m-2] = right_top

# 둘레
r = (N - 1)*2 + (M - 1)*2
# depth 구하기
depth = min(M, N) // 2

for i in range(depth):
    for _ in range(R % r):  # 회전 압축
        rotate(i, i, N-i, M-i)
    r -= 8

for nb in range(N):
    print(*board[nb])
