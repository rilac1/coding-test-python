# 계단 오르기
import sys
input = sys.stdin.readline
N = int(input())
steps = [0] * 300
for i in range(N):
    steps[i] = int(input())

dp = [0] * 300
dp[0], dp[1] = steps[0], steps[0]+steps[1]
dp[2] = max(steps[0]+steps[2], steps[1]+steps[2])
for i in range(3, N):
    dp[i] = max(dp[i-3]+steps[i-1]+steps[i], dp[i-2]+steps[i])

print(dp[N-1])