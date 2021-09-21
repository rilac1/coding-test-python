N, r, c = map(int,input().split())
graph = [[0]*N for _ in range(N)]

inter = 2^(N-2)
dx = [0,0,-1,1]
dy = [0,1,-1,0]

def Z(x,y,n):
    for i in range(4):
        x, y = x+dx[i], y+dy[i]
        graph[x][y] = i+n
    return Z()

x,y,n = 0,0,0
for i in range(inter):
    ...