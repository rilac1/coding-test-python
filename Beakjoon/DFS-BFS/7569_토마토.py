# 토마토
## 3차원 리스트
import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = [0,0,0,0,-1,1]
dy = [-1,0,1,0,0,0]
dz = [0,1,0,-1,0,0]

q = deque()
cnt = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m]==1: q.append((h,n,m,0))
            elif graph[h][n][m]==0: cnt += 1
if not cnt: q=[]

ans = 0
while q:
    x,y,z,ans = q.popleft()
    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0<=nx<H and 0<=ny<N and 0<=nz<M:
            if graph[nx][ny][nz]==0:
                graph[nx][ny][nz]=1
                cnt -= 1
                q.append((nx,ny,nz,ans+1))
if cnt: ans = -1
print(ans)