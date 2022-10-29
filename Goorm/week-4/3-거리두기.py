N = int(input())
dp = [[0] * 5 for _ in range(N)]
dp[0] = [1] * 5

condition = [
    [0, 1, 2, 3, 4],
    [0, 2, 3],
    [0, 1, 3, 4],
    [0, 1, 2],
    [0, 2]
]

for n in range(1, N):
    for i in range(5):
        for j in condition[i]:
            dp[n][i] += dp[n-1][j]
        dp[n][i] %= 100000007

print(sum(dp[-1]) % 100000007)
