from collections import deque
from copy import deepcopy

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

tree_q = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            tree_q.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

day = 0
while tree_q:
    copied_graph = deepcopy(graph)

    for _ in range(len(tree_q)):
        x, y = tree_q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<N and 0<=ny<N and not graph[nx][ny]:
                copied_graph[x][y] -= 1

            if copied_graph[x][y] == 0:
                break

        if copied_graph[x][y]:
            tree_q.append((x, y))

    graph = copied_graph
    day += 1

print(day)
