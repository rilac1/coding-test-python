# Dijkstra
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = [int(j) for j in input().rstrip()]
distance = [[1e9]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

heap = []
heapq.heappush(heap, (1, (0,0)))
while heap:
    dis, (a,b) = heapq.heappop(heap)
    if not 0<=a<N or not 0<=b<M or graph[a][b]==0:
        continue
    graph[a][b] = 0
    if dis <= distance[a][b]:
        distance[a][b] = dis
        for i in range(4):
            heapq.heappush(heap, (dis+1, (a+dx[i], b+dy[i])))

print(distance[N-1][M-1])