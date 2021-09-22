# 파티
import sys, heapq
input = sys.stdin.readline
N,M,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph_r[b].append((a,t))

def dijkstra(start):
    dist=[1e9]*(N+1)
    h=[(0,start)]
    while h:
        cost,a = heapq.heappop(h)
        if cost<dist[a]:
            dist[a]=cost
            for b,c in graph[a]:
                heapq.heappush(h,(cost+c,b))
    return dist

departure = dijkstra(X)
graph = graph_r
arrival = dijkstra(X)
for i in range(1,N+1):
    departure[i] += arrival[i]
departure[0]=0
print(max(departure))
