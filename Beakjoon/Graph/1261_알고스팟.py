# 알고스팟
## Dijkstra
import heapq
M,N = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[1e9]*M for _ in range(N)]
visited[0][0] = 0
q = [(0,(0,0))]
while q:
    cost,(x,y) = heapq.heappop(q)
    if cost!=visited[x][y]: continue
    if x==N-1 and y==M-1: break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]: c = cost+1
            else: c = cost
            if c<visited[nx][ny]:
                visited[nx][ny] = c
                heapq.heappush(q, (c,(nx,ny)))
print(visited[N-1][M-1])