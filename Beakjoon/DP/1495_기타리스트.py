# 기타리스트
import sys
input = sys.stdin.readline
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [set([]) for _ in range(N+1)]
dp[0].add(S)

for i in range(N):
    d = V[i]
    for j in dp[i]:
        if 0<=j+d<=M:
            dp[i+1].add(j+d)
        if 0<=j-d<=M:
            dp[i+1].add(j-d)
    
if dp[N]:
    print(max(dp[N]))
else:
    print(-1)