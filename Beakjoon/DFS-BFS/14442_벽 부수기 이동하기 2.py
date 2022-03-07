# 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[-1]*(M+1) for _ in range(N+1)]

visited[0][0] = K
q = deque([(0,0,K,1)])

while q:
    x,y,wall,cnt = q.popleft()

    if x==N-1 and y==M-1:
        print(cnt)
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        w = wall
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]: w -= 1
            if visited[nx][ny] < w: 
                visited[nx][ny] = w
                q.append((nx,ny, w, cnt+1))
print(-1)