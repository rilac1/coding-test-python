from collections import deque
import sys
input = sys.stdin.readline
q = deque([])
for _ in range(int(input())):
    cmd = input().split()
    c=cmd[0]
    if c=='push': deque.append(q, cmd[1])
    elif c=='size': print(len(q))
    elif c=='empty': print(int(len(q)==0))
    elif not q: print(-1)
    elif c=='pop': print(deque.popleft(q))
    elif c=='front': print(q[0])
    elif c=='back': print(q[-1])