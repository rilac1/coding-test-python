# 로봇 청소기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r,c,d = map(int, input().split())
stage = []
for _ in range(N):
    stage.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ret = 0

while True:
    if stage[r][c] == 0:
        stage[r][c] = 2
        ret += 1
    if stage[r][c] == 1:
        break

    for i in range(4):    
        d = (d-1)%4
        x = r+dx[d]
        y = c+dy[d]
        
        if stage[x][y]==0:
            r, c = x, y
            break
        if i==3:
            r -= dx[d]
            c -= dy[d]

print(ret)