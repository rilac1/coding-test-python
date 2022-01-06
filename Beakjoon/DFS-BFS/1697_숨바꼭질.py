# 숨바꼭질
## BFS
from collections import deque
N, K = map(int, input().split())
visited = [False]*200000
q = deque()
deque.append(q,(N,0))
while q:
    point, time = deque.popleft(q)
    if point==K:
        print(time)
        break
    if point<K:
        if not visited[point*2]:
            visited[point*2] = True
            deque.append(q,(point*2, time+1))
        if not visited[point+1]:
            visited[point+1] = True
            deque.append(q,(point+1, time+1))
    if point>0 and not visited[point-1]:
        visited[point-1] = True
        deque.append(q,(point-1, time+1))
