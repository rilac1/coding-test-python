# 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(x,y):
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]:
            dfs(nx,ny)

for _ in range(T):
    M,N,K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                cnt += 1
                dfs(i,j)
    print(cnt)