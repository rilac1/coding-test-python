# 가장 긴 증가하는 부분 수열
N = int(input())
a = list(map(int,input().split()))

dp = [0]*(N)
for i in range(N):
    for j in range(i):
        if a[j]<a[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))