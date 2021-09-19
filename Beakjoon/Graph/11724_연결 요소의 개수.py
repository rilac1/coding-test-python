# 연결 요소의 개수
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)	

def dfs(a):
	visited[a]=True
	for i in graph[a]:
		if not visited[i]:
			dfs(i)

ret = 0
visited = [False]*(N+1)
for i in range(1,N+1):
	if not visited[i]:
		ret += 1
		dfs(i)
		
print(ret)


## Union-Find
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)	

parent = list(range(N+1))
for i in range(1,N+1):
    for j in graph[i]:
        if parent[i] != j:
            parent[j]=parent[i]

print(len(set(parent))-1)