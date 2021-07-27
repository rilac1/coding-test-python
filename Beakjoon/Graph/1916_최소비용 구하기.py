# Dijkstra
import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

h = []
distance = [1e9] * (N+1)
heapq.heappush(h, (0, start))
while h:
    cost, city = heapq.heappop(h)
    if cost < distance[city]:
        distance[city] = cost
        for ci, co in graph[city]:
            heapq.heappush(h,(cost+co, ci))

print(distance[end])