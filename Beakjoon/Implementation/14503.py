import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r,c,d = map(int, input().split())
stage = []
for _ in range(N):
    stage.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ret = 0

while True:
    if stage[r][c]==1:
        break
    if stage[r][c]==0:
        stage[r][c] = 2
        ret += 1
    for i in range(4):    
        d = (d-1)%4
        if stage[r+dx[d]][c+dy[d]]==0:
            break
        if i==3:
            d = (d-1)%4
            r -= dx[d]
            c -= dy[d]

print(ret)