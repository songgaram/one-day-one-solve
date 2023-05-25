import itertools

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# combination = itertools.combinations(range(N), N//2)
# combi = list(combination)


# min_dis = 100
# for c in combi:
#     start = 0
#     link = 0
#     for i in range(N):
#         for j in range(N):
#             if i in c and j in c:
#                 start += field[i][j]
#             elif i not in c and j not in c:
#                 link += field[i][j]
#     dis = abs(start - link)
#     min_dis = min(dis, min_dis)

# print(min_dis)

visited = [False] * N
def dfs(d, idx):
    global min_d
    if d == N // 2:
        start = 0
        link = 0
        for a in range(N):
            for b in range(N):
                if visited[a] and visited[b]:
                    start += field[a][b]
                elif not visited[a] and not visited[b]:
                    link += field[a][b]
        min_d = min(abs(start-link), min_d)
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(d+1, i)
            visited[i] = False

min_d = 100
dfs(0, 0)
print(min_d)
