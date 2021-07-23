import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

#####   DFS   ######
visited = [False]*(N+1)
def dfs(a):
    if visited[a]:
        return
    print(a, end=' ')
    visited[a] = True
    for i in graph[a]:
        dfs(i)
dfs(V)
print()

#####   BFS   ######
visited = [False]*(N+1)
queue = deque([V])
while queue:
    a = queue.popleft()
    if visited[a]:
        continue
    print(a, end=' ')
    visited[a] = True
    for i in graph[a]:
        queue.append(i)
print()