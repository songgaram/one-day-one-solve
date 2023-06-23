"""
1) top-down 방식으로 해야 시간초과 나지 않음
for i in (3,2,n):
    if i == n: 
    elif num % i == 0 
2) elif로 하면 만약 2와 n이 같으면 2로 나누지 못한다.
    if i == n: 
    if num % i == 0 
3) if로 바꿨으나, 이번에도 n으로 나눠진다면 나눠버리기 때문에 안됨.
    if i == n:
    if i % 3 == 0 or i % 2 == 0:
4) 이건 3 또는 2로 나눠지는 조건이라서 3으로 나눠지는데 2로는 안나눠지는 경우 발생
"""


from collections import deque
def solution(x, y, n):
    visited = [False] * 10000000
    def bfs(x, y, n):
        q = deque()
        q.append([y, 0])
        visited[y] = True
        nxt = 0
        while q:
            num, cnt = q.popleft()
            if num == x:
                return cnt
            for i in (3, 2, 0):
                if i == 0:
                    nxt = num - n
                elif num % i == 0:
                    nxt = num // i
                if not visited[nxt]:        
                    if nxt >= x:
                        q.append([nxt, cnt+1])
                        visited[nxt] = True
                
        return -1
    a = bfs(x, y, n)
    return a