from collections import deque
import copy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate(board):
    rotated = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][N-j-1] = board[i][j]
    return rotated


def play(d, board):
    for _ in range(d):
        board = rotate(board)
    for i in range(N):
        q = deque(board[i])
        new_arr = []
        while q:
            board = q.popleft()
            if board != 0:
                if not q:
                    new_arr.append(board)
                    break
                if board != q[0]:
                    new_arr.append(board)
                else:
                    new_arr.append(board * 2)
                    q.popleft()
        board[i] = new_arr
    return board

def check():
    return

def dfs(depth, board):
    if depth == 5:
        check()
    temp = copy.deepcopy(board)
    for d in range(4):
        play(d, temp)
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)

dfs(0, board)

