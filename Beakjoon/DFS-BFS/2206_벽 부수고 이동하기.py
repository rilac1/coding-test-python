import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, str(input().rstrip()))) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[[0]*2 for _ in range(M)] for __ in range(N)]

def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        x, y, broken = q.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][broken]+1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not 0<=nx<N or not 0<=ny<M:
                continue
            elif graph[nx][ny]==0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = visited[x][y][broken]+1
                q.append((nx,ny,broken))
            elif graph[nx][ny]==1 and not broken:
                visited[nx][ny][1] = visited[x][y][broken]+1
                q.append((nx,ny,1))

ret = bfs()
if ret: print(ret)
else:   print(-1)