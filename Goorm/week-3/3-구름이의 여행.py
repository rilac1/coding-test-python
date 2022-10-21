import sys, heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
visited[1] = True
q = [(0,1)]

while q:
    dis, node = heapq.heappop(q)
    if node == N and dis <= K:
        print('YES')
        exit(0)

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            heapq.heappush(q, (dis+1, next_node))

print('NO')
