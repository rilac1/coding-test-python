# 트리의 지름
import sys, heapq
input=sys.stdin.readline
V = int(input())
graph = [[]for _ in range(V+1)]
for _ in range(V):
    temp=list(map(int, input().split()))
    a = temp[0]
    i = 1
    while True:
        if temp[i]==-1: break
        b, dis = temp[i], temp[i+1]
        graph[a].append((b,dis))
        i += 2

def dijkstra(a):
    h = [(0,a)]
    distance = [1e9]*(V+1)
    while h:
        dis,b = heapq.heappop(h)
        if dis<distance[b]:
            distance[b] = dis
            for i,d in graph[b]:
                heapq.heappush(h, ((d+dis,i)))
    return distance

d = dijkstra(1)
picked = d.index(max(d[1:]))
print(max(dijkstra(picked)[1:]))