# 가장 긴 증가하는 부분 수열
N = int(input())
a = list(map(int,input().split()))

dp = [1]*(N)
for i in range(N-1):
    if a[i]<a[i+1]:
        dp[i+1] = dp[i]+1
    else:
        j = i-1
        while a[j]>a[i] and j>0: 
            j -= 1 
        if a[j]==a[i]: dp[i] = dp[j]
        elif a[j]<a[i]: dp[i] = dp[j]+1
print(dp)


# 2 4 6 8 5 3 4 5 6 3
# 1 2 3 4 3 2 3 4 5 2 