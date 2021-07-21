# 바이러스
# 탐색
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for a in graph[x]:
        dfs(a)

dfs(1)
ret = 0
for i in visited[2:]:
    if i:
        ret += 1

print(ret)