# 퇴사
N = int(input())
T, P = [], []
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

dp = [0]*(N+1)
for i in range(N):
    n = i+T[i]
    for j in range(n,N+1):
        dp[j] = max(dp[j], dp[i]+P[i])
print(dp[-1])