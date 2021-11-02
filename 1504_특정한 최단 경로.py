import sys, heapq
input = sys.stdin.readline
N,E = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int, input().split())

def dij(a):
    dist = [1e9]*(N+1)
    h = [(0,a)]
    while h:
        c,b = heapq.heappop(h)
        if dist[b]<c:
            continue
        for t,d in graph[b]:
            if c+d<dist[t]:
                dist[t] = c+d
                heapq.heappush(h,(c+d,t))
    return dist
d0 = dij(1)
d1 = dij(v1)
d2 = dij(v2)
if d0[v1]>=1e9 or d0[v2]>=1e9 or d0[N]>=1e9:
    print(-1)
else:
    print(min(d0[v1]+d1[v2]+d2[N], d0[v2]+d2[v1]+d1[N]))