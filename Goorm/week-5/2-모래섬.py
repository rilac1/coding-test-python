from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

water_q = deque()
ground_set = set()

def init():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                deque.append(water_q, (i, j))
            else:
                ground_set.add((i, j))


def water_up():
    for _ in range(len(water_q)):
        x, y = water_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                ground_set.remove((nx, ny))
                water_q.append((nx, ny))


def dfs(x, y, ground):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (nx, ny) in ground:
            ground.remove((nx, ny))
            dfs(nx, ny, ground)


init()
ans = 0
while True:
    if not ground_set:
        print(-1)
        exit(0)

    copied_ground_set = deepcopy(ground_set)
    x, y = copied_ground_set.pop()
    dfs(x, y, copied_ground_set)

    if copied_ground_set:
        print(ans)
        exit(0)

    water_up()
    ans += 1
