# 최단경로
## 다익스트라(dijkstra)
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[]for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

dist = [1e9] * (V+1)
h = []
heapq.heappush(h, (0, K))
while h:
    cost, next = heapq.heappop(h)
    if cost < dist[next]:
        dist[next] = cost
        for n, c in graph[next]:
            heapq.heappush(h, (c+cost, n))

for i in dist[1:]:
    if i == 1e9:
        print('INF')
    else:
        print(i)