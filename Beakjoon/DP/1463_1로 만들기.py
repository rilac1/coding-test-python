N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    temp=True
    if i%2==0:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        temp=False
    if i%3==0:
        dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        temp=False
    if temp:
        dp[i] = dp[i-1]+1

print(dp[N])