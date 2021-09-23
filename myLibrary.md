## Dijkstra
```python
import heapq
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
```

## UnionFind
```python
def find(x):
    if x==parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]
```