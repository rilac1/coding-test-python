import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

case = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    visited[0][0] = True
    q = [(graph[0][0], 0, 0)]

    while q:
        rupee, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            print("Problem {0}: {1}".format(case, rupee))
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(q, (rupee + graph[nx][ny], nx, ny))

    case += 1
