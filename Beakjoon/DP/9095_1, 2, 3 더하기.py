# 1,2,3, 더하기
import sys
input = sys.stdin.readline

T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))

dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for n in N:
    print(dp[n])