# 줄 세우기
## 위상정렬
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
comp = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(M):
    a,b = map(int, input().split())
    degree[b] += 1
    comp[b].append(a)

start = 0
for i in range(1,N+1):
    if degree[i]==0:
        start = i
        break

q = deque([start])
while q:
    a = deque.popleft(q)
    print(a, end=' ')
    for b in comp[a]:
        degree[b] -= 1
        if degree[b]==0: deque.append(q, b)
print()