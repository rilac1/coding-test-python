# 아기 상어
import sys, heapq
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

fish=[]
while q or fish:
    if not q and fish:
        nx,ny = fish[0]
        fish=[]

        graph[nx][ny]=0
        eat+=1
        if eat==size:
            eat=0
            size+=1
    
        visited = [[False]*N for _ in range(N)]
        ret += limit
        limit=1e9
        deque.append(q, (nx,ny,0))
        continue
    
    x,y,cnt = deque.popleft(q)
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if cnt<limit and 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            visited[nx][ny] = True
            temp=graph[nx][ny]
            if 0<temp<size:
                limit = cnt+1
                heapq.heappush(fish, (nx,ny))
            elif temp==0 or temp==size:
                deque.append(q, (nx,ny,cnt+1))
print(ret)