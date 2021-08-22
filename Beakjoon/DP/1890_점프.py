# 점프
import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]
def dfs(x,y):
    if x==N-1 and y==N-1:
        return 1
    if dp[x][y] ==-1:
        dp[x][y] = 0
        nx = x + graph[x][y]
        ny = y + graph[x][y]
        if 0<=nx<N:
            dp[x][y] += dfs(nx,y)
        if 0<=ny<N:
            dp[x][y] += dfs(x,ny)
    return dp[x][y]

print(dfs(0,0))