import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
graph=[[]for _ in range(N+1)]
for i in range(1,N):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parents=[0]*(N+1)
visited = [False]*(N+1)
visited[1]=True
q = deque([1])
while q:
    g = deque.popleft(q)
    for i in graph[g]:
        if not visited[i]:
            visited[i]=True
            parents[i]=g
            deque.append(q,i)

for i in parents[2:]:
    print(i)