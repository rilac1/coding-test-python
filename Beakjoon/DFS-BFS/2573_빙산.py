# 빙산
from collections import deque
from copy import deepcopy
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

iceberg = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]: iceberg.append((i,j))

def isSplited():
    visited = [[False]*M for _ in range(N)]
    q = deque()
    if iceberg: q.append(iceberg[0])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]>0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

    for x,y in iceberg:
        if not visited[x][y]:
            return True
    return False

cnt = 0
while not isSplited():
    if not iceberg:
        cnt = 0
        break
    graph_copy = deepcopy(graph)
    for _ in range(len(iceberg)):
        x,y = iceberg.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                graph_copy[x][y] -= 1
        if graph_copy[x][y]>0: iceberg.append((x,y))
        else: graph_copy[x][y] = 0
    graph = graph_copy
    cnt += 1
print(cnt)