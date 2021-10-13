# 벽 부수고 이동하기 4
import sys
sys.setrecursionlimit(9999999)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
table = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def dfs(x,y):
    cnt = 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]==0:
                if not visited[nx][ny]:
                    cnt += dfs(nx,ny)
            elif not check[nx][ny]:
                check[nx][ny] = True
                wall.append((nx,ny))
    return cnt
        
for i in range(N):
    for j in range(M):
        if graph[i][j]==0 and not visited[i][j]:
            wall = []
            check = [[False]*M for _ in range(N)]
            cnt = dfs(i,j)
            for x,y in wall:
                table[x][y] += cnt

for i in range(N):
    for j in range(M):
        temp=table[i][j]
        if temp: print(temp+1,end='')
        else: print(temp,end='')
    print()