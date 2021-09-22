# 특정 거리의 도시 찾기
import sys, heapq
input = sys.stdin.readline
N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

dist=[1e9]*(N+1)
h=[(0,X)]
while h:
    c,a = heapq.heappop(h)
    if c<dist[a]:
        dist[a]=c
        for b in graph[a]:
            heapq.heappush(h,(c+1,b))

flag=True
for i in range(1,N+1):
    if dist[i]==K:
        flag=False
        print(i)
if flag: print(-1)