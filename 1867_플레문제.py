import sys
input = sys.stdin.readline
n,k = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b] = 1

    \\₩