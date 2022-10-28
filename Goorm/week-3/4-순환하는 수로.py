import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
graph = [set() for _ in range(N+1)]

for _ in range(N):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def delete_leaf_node(node):
    path_set = graph[node]
    if len(path_set) == 1:
        target = path_set.pop()
        graph[target].remove(node)
        delete_leaf_node(target)

for node in range(1, N+1):
    delete_leaf_node(node)

answer = [node for node in range(1, N+1) if len(graph[node]) == 2]
print(len(answer))
print(*answer)
