# 안전영역
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0,1,0,-1], [-1,0,1,0]
m = max(map(max, graph))
def dfs(x,y):
    global h
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            visited[nx][ny] = True
            if graph[nx][ny]>h:
                dfs(nx,ny)

ans = 0
for h in range(m):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j]>h:
                cnt += 1
                dfs(i,j)
    ans = max(ans, cnt)

print(ans)