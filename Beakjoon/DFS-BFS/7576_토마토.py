# 토마토
import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            deque.append(q, (i,j,0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while q:
    x,y,n = deque.popleft(q)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            graph[nx][ny]=1
            deque.append(q, (nx,ny, n+1))
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            print(-1)
            exit(0)
print(n)