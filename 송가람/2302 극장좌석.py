import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1

def fibo(num):
    if dp[num] != 0:
        return dp[num]
    dp[num] = fibo(num-1) + fibo(num-2)
    return dp[num]

fibo(n)
seat = list(range(1, n+1))
count = 1
vip = []
for i in range(m):
    fixed_seat = int(input().rstrip())
    vip.append(fixed_seat-1)

start = 0
count = 1
for i in range(m):
    size = len(seat[start:vip[i]])
    cases = dp[size]
    count *= cases
    start = vip[i] + 1

size = len(seat[start:n])
cases = dp[size]
count *= cases
print(count)