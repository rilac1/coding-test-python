from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def is_survive(x, y):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    q = deque([(x, y)])

    for _ in range(M):
        for _ in range(len(q)):
            x, y = deque.popleft(q)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    if graph[nx][ny] == 2:
                        return True
                    visited[nx][ny] = True
                    deque.append(q, (nx, ny))
    return False

ans = 0
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            ans += int(is_survive(x, y))
print(ans)
