# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            house.append((i,j))

def checkDis(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

while house:
    a,b = house.popleft()
    

