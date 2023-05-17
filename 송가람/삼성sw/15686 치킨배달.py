import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

def distance(a, b):
    ay, ax = a
    by, bx = b
    return abs(ay - by) + abs(ax - bx)

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            home.append([i, j])

ans = []
while M > 0:
    comb_chicken = list(combinations(chicken, M))

    for k in range(len(comb_chicken)):
        all_dis = [0] * len(home)
        for l in comb_chicken[k]:
            for n in range(len(home)):
                dis = distance(l, home[n])
                if all_dis[n] == 0 or all_dis[n] > dis:
                    all_dis[n] = dis

        ans.append(sum(all_dis))
    M -= 1
    
print(min(ans))
            


