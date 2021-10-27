# 벽 부수고 이동하기 4
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False]*M for _ in range(N)]

def bfs(x,y):
    cnt = 0
    visited[x][y] = True
    q = deque()
    deque.append(q, (x,y))
    while q:
        cnt += 1
        x,y = deque.popleft(q)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny]==0: deque.append(q, (nx,ny))
                else: wall.append((nx,ny))
    return cnt

for i in range(N):
    for j in range(M):
        if graph[i][j]==0 and not visited[i][j]:
            wall = []
            cnt = bfs(i,j)
            for x,y in wall:
                graph[x][y] += cnt
                visited[x][y] = False

for i in range(N):
    for j in range(M):
        if graph[i][j]: graph[i][j]%=10
        print(graph[i][j], end='')
    print()