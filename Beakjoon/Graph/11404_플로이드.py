# 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(n+1):
    graph[i][i] = 0

for temp in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][temp] + graph[temp][b])

for i in graph[1:]:
    for j in i[1:]:
        if j==INF:
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()