# 영역 구하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
M,N,K = map(int,input().split())
graph = [[0]*N for _ in range(M)]

dx,dy = [-1,0,1,0], [0,1,0,-1]

def dfs(x,y):
    global area
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[nx][ny]==0:
            graph[nx][ny] = 1
            area += 1
            dfs(nx,ny)
        
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x] = 1

ans = []
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            graph[i][j] = 1
            area = 1
            dfs(i,j)
            ans.append(area)

print(len(ans))
print(*sorted(ans))