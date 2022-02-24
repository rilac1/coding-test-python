# 경사로
import sys
input = sys.stdin.readline
N,L = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx,dy = [1,0],[0,1]

def dfs(x,y,l,d):
    nx,ny = x+dx[d], y+dy[d]
    if nx==N or ny==N:
        return 1
    if graph[x][y]==graph[nx][ny]:
        return dfs(nx,ny,l+1,d)
    elif (graph[nx][ny]-graph[x][y])==1 and l>=L:
        return dfs(nx,ny,1,d)

    l = 0
    while graph[nx][ny]==(graph[x][y]-1):
        l += 1
        nx += dx[d]
        ny += dy[d]
        if nx==N or ny==N:
            break
    if l>=L:
        return dfs(nx-dx[d],ny-dy[d],l-L,d)
    return 0

ans = 0
for i in range(N):
    ans += dfs(0,i,1,0)
    ans += dfs(i,0,1,1)
print(ans)