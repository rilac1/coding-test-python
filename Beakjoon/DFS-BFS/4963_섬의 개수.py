# 섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def dfs(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        if graph[x][y]:
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<h and 0<=ny<w:
                    dfs(nx,ny)
            return 1
    return 0
        
while True:
    w, h = map(int,input().split())
    if w+h == 0: break
    cnt = 0
    visited = [[False]*w for _ in range(h)]
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            cnt += dfs(i,j)
    print(cnt)