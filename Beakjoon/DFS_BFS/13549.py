import heapq
import sys
N, K = map(int, input().split())
q = []
heapq.heappush(q,(0, N))
distance = [sys.maxsize] * 100001
distance[N] = 0

while q:
    dist, x = heapq.heappop(q)
    if dist > distance[x]:
        continue
    else:
        distance[x] = dist
    if 0<=x<=K:
        heapq.heappush(q, (dist, x*2))
    for i in (x+1, x-1):
        if 0<=i<=100000:
            heapq.heappush(q, (dist+1, i))

print(distance[K])

"""
from collections import deque
N, K = map(int, input().split())
min_path = [-1] * 100001
min_path[N] = 0

queue = deque([N])
while queue:
    x = queue.popleft()
    temp = x*2
    if 0<=temp<=100000:
        if min_path[temp] == -1:
            min_path[temp] = min_path[x]
            queue.append(temp)

    for i in range(x+1, x-1):
        if min_path[i] == -1:
            min_path[i] = min_path[x] + 1
            queue.append(i)

print(min_path[K])
"""