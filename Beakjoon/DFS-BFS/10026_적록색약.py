# 적록색약
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
graph1 = [list(input().rstrip()) for _ in range(N)]
graph2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        temp = graph1[i][j]
        if temp == 'R':
            temp = 'G'
        graph2[i][j] = temp

dx = [0,1,0,-1]
dy = [-1,0,1,0]
a,b = 0,0

def dfs(x,y,color):
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny]==color:
            dfs(nx,ny,color)
            
for i in range(N):
    for j in range(N):
        graph = graph1
        color = graph[i][j]
        if color:
            a += 1
            dfs(i,j,color)
            
        graph = graph2
        color = graph[i][j]
        if color:
            b += 1
            dfs(i,j,color)

print(a,b)