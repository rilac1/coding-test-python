import sys
from copy import deepcopy
input = sys.stdin.readline

def dfs(node, parent, answer):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            answer.append(next)
            return dfs(next, node, deepcopy(answer))

        elif next != parent:
            return answer
    return []

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

max_length = 0
for node in range(1, N):
    visited = [False] * (N+1)
    result = dfs(node, -1, [0])
    if max_length < len(result):
        answer = result
        max_length = len(answer)

answer.sort()
print(len(answer))
print(answer)
