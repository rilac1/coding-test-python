# 1학년
N = int(input())
arr = list(map(int,input().split()))

dp = [[0]*21 for _ in range(N)]
dp[0][arr[0]] = 1
for idx in range(N-1):
    for result in range(21):
        if dp[idx][result]:
            next = (result+arr[idx+1], result-arr[idx+1])
            for n in next:
                if 0<=n<=20: dp[idx+1][n] += dp[idx][result]
print(dp[N-2][arr[N-1]])