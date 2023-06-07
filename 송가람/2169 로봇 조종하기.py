import sys, copy
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, M):
    board[0][i] += board[0][i-1]

dp = [0] * (M)
for n in range(N-1):
    # 오른쪽 더하기 => 
    right = copy.deepcopy(board[n+1]) 
    right[0] += board[n][0]
    for i in range(1, M):
        right[i] = max(right[i-1] + right[i], board[n][i] + right[i])

    # <= 왼쪽 더하기
    left = copy.deepcopy(board[n+1])
    left[-1] += board[n][-1]
    for j in range(M-2, -1, -1):
        left[j] = max(left[j+1] + left[j], board[n][j] + left[j])

    # 오른쪽 왼쪽 합치기
    for idx in range(M):
        dp[idx] = max(right[idx], left[idx])
    
    board[n+1] = dp


print(board[N-1][M-1])

