from collections import deque
import copy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate(board):
    rotated = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][N-i-1] = board[i][j]
    return rotated

def rerotate(board):
    rotated = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[N-j-1][i] = board[i][j]
    return rotated

def play(d, board):
    for _ in range(d):
        board = rotate(board)
    for i in range(N):
        new_arr = [0] * N
        pointer = 0
        for j in range(N):
            # 0이면 패스 0아니면 할당
            if board[i][j] != 0:
                temp = board[i][j]
                # 새로운 배열 값이 0이면 바로 현재 값 할당
                if new_arr[pointer] == 0:
                    new_arr[pointer] = temp
                # 현재 값이랑 같을 경우
                elif new_arr[pointer] == temp:
                    new_arr[pointer] = temp*2
                    pointer += 1
                # 현재 값이랑 같지 않고 0도 아닌 경우 다음 칸에 할당
                else:
                    pointer += 1
                    new_arr[pointer] = temp
        board[i] = new_arr
    for _ in range(d):
        board = rerotate(board)
    return board


def check(board):
    max_block = 0
    for i in range(N):
        max_block = max(max_block, max(board[i]))
    return max_block

def dfs(depth, board):
    global max_block
    if depth == 5:
        max_block = max(max_block, check(board))
        return
    temp = copy.deepcopy(board)
    for d in range(4):
        temp = play(d, temp)
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)

max_block = 2
dfs(0, board)
print(max_block)

"""
3
0 64 8
128 0 32
32 0 0
256
"""

