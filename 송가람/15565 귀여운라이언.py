N, K = map(int, input().split())
dolls = list(map(int, input().split()))

start, end = 0, 0
total = 0
min_d = 10**6
total = 1 if dolls[0] == 1 else total

while start <= end and end < N:
    if total < K:
        if end == N - 1:
            break
        end += 1
        if dolls[end] == 1:
            total += 1 
    elif total >= K:
        if dolls[start] == 1:
            total -= 1 
        start += 1
    
    if total >= K:
        if end - start + 1 < min_d:
            min_d = end - start + 1

if min_d == 10**6:
    print(-1)
else:
    print(min_d)

