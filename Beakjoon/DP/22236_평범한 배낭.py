# 평범한 배낭
d,m = map(int, input().split())
dp = [[0]*(d//2+2) for _ in range(d)]
dp[0][0] = 1
for i in range(d-1):
    for j in range(1, min(i+2, d-i)):
        dp[i+1][j] = dp[i][j+1] + dp[i][j-1]
print(dp[d-1][1]%m)