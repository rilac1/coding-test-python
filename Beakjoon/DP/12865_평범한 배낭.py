# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [(0,0)]
for _ in range(N):
    w, v = map(int, input().split())
    stuff.append((w,v))

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = stuff[i][0], stuff[i][1]
    for j in range(1, K+1):
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])