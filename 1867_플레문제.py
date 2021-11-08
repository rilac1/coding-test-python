import sys
input = sys.stdin.readline
n,k = map(int, input().split())
row, col = [0]*n, [0]*n
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b] = 1
    row[a] += 1
    col[b] += 1

ans = 0
while n:
    r, c = max(row), max(col)
    if r>=c:
        for i in graph:
            ...