# 퇴사2
import sys
input = sys.stdin.readline
N = int(input())
table = [[] for _ in range(N+1)]

for i in range(1, N+1):
    t,p = map(int, input().split())
    table[i] = (t, p)
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])
    time = table[i][0] - 1
    price = table[i][1]
    if i + time <= N:
        dp[i+time] = max(dp[i+time], dp[i-1]+price)

print(dp[N])