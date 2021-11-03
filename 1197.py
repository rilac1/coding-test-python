# 최소 스패닝 트리
## 벨만포드
import sys
input = sys.stdin.readline
V,E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    A,B,C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

upper = [1e9]*(V+1)
restart = True
while restart:
    restart = True