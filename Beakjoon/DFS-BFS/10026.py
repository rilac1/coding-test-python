# 적록색약
import sys
input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0,1,-1,0]
dy = [-1,0,1,0]

def dfs(x,y,color):
    global cnt
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny]==color:
                dfs(nx,ny,color)
            elif graph[nx][ny]!=0:
                cnt += 1
                dfs(nx,ny,graph[nx][ny])
            
cnt=0
dfs(0,0,0)
print(cnt)