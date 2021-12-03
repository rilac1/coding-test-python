# 스타트링크
from collections import deque
F, S, G, U, D = map(int, input().split())
vist = [False]*(F+1)
vist[S] = True
q = deque([(S,0)])
while q:
    s,c = deque.popleft(q)
    if s==G:
        print(c)
        exit(0)
    for n in (s+U, s-D):
        if 0<n<=F and not vist[n]: 
            vist[n] = True
            deque.append(q, (n,c+1))
print("use the stairs")