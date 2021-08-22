# 치킨 배달
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

def checkDis(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

ret = 0
for h in house:
    mindis = 1e9
    for c in chicken:
        mindis = min(mindis, checkDis(h,c))
    print(mindis)
    ret += mindis



print(ret)