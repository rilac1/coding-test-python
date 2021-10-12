# 앱
## Hint...
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))
limit = sum(c)

dp = [0]*(limit+1)
for i in range(1, N+1):
    for j in range(limit, c[i]-1, -1):
        dp[j] = min(max(dp[j], dp[j-c[i]]+m[i]), M)
print(dp.index(M))