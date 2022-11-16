import heapq

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (N+1)
visited[K] = True
q = [(0, K)]

while q:
    cost, current_node = heapq.heappop(q)
    for next_node in graph[current_node]:
        if next_node == K:
            print(cost+1)
            exit(0)

        if not visited[next_node]:
            visited[next_node] = True
            heapq.heappush(q, (cost+1, next_node))

print(-1)
