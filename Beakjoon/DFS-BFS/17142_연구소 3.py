# 연구소 3
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1,0,1,0], [0,1,0,-1]

virus = []
target = 0
for i in range(N):
    for j in range(N):
            if graph[i][j] == 0: target += 1
            if graph[i][j] == 2: virus.append((i,j))

queue = deque()
ans = 1e9

def comb(left):
    global ans
    if len(queue)==M:
        ans = min(ans, bfs(deepcopy(graph), deepcopy(queue)))
    else:
        for i in range(left, len(virus)):
            a,b = virus[i]
            graph[a][b] = 1
            queue.append((a,b))
            comb(i+1)
            queue.pop()
            graph[a][b] = 2

def bfs(g, q):
    cnt,t = 0, target
    while q:
        if t==0: return cnt
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N and g[nx][ny]!=1:
                    if g[nx][ny]==0: t -= 1
                    g[nx][ny] = 1
                    q.append((nx,ny))
        cnt += 1
    return 1e9

comb(0)
if ans==1e9: ans = -1
print(ans)