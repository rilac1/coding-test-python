N, M, K = map(int, input().split())

dp = [[0] * (N+M+1) for _ in range(K+1)]

for game in range(K):
    for marble in range(N+M+1):
        if marble==0 or marble == N+M:
            dp[game][marble] = 1
        for d in [-1, 0, 1]:
            if 0 < marble+d < N+M:
                dp[game+1][marble+d] += dp[game][marble]

print(dp[K][N] % 100000007)
