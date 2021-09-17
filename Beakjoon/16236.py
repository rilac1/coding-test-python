# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            deque.append(q, (i,j,0))
            graph[i][j]=0

dx = [-1,0,0,1]
dy = [0,-1,1,0]
size,eat,ret,limit = 2,0,0,1e9
visited = [[False]*N for _ in range(N)]
fish = []

while q or fish:
    if not q and fish:
        fish.sort()
        dis,a,b=fish[0]
        graph[a][b]=0
        eat += 1
        if eat==size:
            eat = 0
            size += 1
        
        visited = [[False]*N for _ in range(N)]
        limit = 1e9
        ret += dis+1
        deque.append(q, (a,b,0))
        continue

    x, y, cnt = deque.popleft(q)
    visited[x][y] = True
    if cnt>=limit: 
        continue
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny]<=size:
            if 0<graph[nx][ny]<size:
                if not fish: limit = cnt
                fish.append((cnt,nx,ny))

            if not visited[nx][ny]:
                deque.append(q, (nx,ny,cnt+1))
print(ret)
