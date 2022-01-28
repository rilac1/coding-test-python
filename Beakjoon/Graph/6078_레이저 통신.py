# 레이저 통신
## Dijkstra, BFS
import sys, heapq
input = sys.stdin.readline
W, H = map(int,input().split())
graph = [input().rstrip() for _ in range(H)]

dx,dy = [-1,0,1,0], [0,1,0,-1]
visited = [[1e9]*W for _ in range(H)]
for b in range(W):
    for a in range(H):
        if graph[a][b]=='C':
            q = [(-1,-1,a,b)]
            visited[a][b] = -1
            break
    if visited[a][b]==-1: break

while q:
    n,d,x,y = heapq.heappop(q)
    if graph[x][y]=='C' and visited[x][y]!=-1:
        print(n)
        break
    if n==visited[x][y]:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W and graph[nx][ny]!='*':
                if i==d: nn = n
                else: nn = n+1
                if nn<=visited[nx][ny]:
                    visited[nx][ny] = nn
                    heapq.heappush(q,(nn,i,nx,ny))