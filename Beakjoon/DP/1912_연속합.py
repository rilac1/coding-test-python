# 연속합
N = int(input())
arr = list(map(int,input().split()))
dp = [0]*N
dp[0], ret = arr[0],arr[0]
for i in range(1, N):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    ret = max(dp[i], ret)
print(ret)