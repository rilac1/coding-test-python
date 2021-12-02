# 촌수계산
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
graph = [[0] for _ in range(n+1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    graph[y][0] = x
    graph[x].append(y)

vist = [False]*(n+1)
vist[0] = True
q = deque([(a,0)])
while q:
    now, c = deque.popleft(q)
    vist[now] = True
    if now==b:
        print(c)
        exit(0)
    for i in graph[now]:
        if not vist[i]: deque.append(q,(i,c+1))
print(-1)