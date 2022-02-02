# 주사위 굴리기
## https://primayy.tistory.com/14 그림만 참고함
import sys
from collections import deque
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dx, dy = [0,0,-1,1], [1,-1,0,0]
row = deque([0]*4)
col = deque([0]*4)

def move(i):
    if i<2:
        if i==0: row.append(row.popleft()) 
        else: row.appendleft(row.pop())
        col[1] = row[1]
        col[3] = row[3]
    else:
        if i==3: col.appendleft(col.pop())
        else: col.append(col.popleft())
        row[1] = col[1]
        row[3] = col[3]

for i in order:
    i-=1
    nx,ny = x+dx[i], y+dy[i]
    if 0<=nx<N and 0<=ny<M:
        move(i)
        x,y = nx,ny
        if graph[x][y]: 
            row[1] = graph[x][y]
            col[1] = graph[x][y]
            graph[x][y] = 0
        else: graph[x][y] = row[1]
        print(row[3])