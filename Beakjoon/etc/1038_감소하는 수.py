# 감소하는 수
## 정석: 백트래킹
from collections import deque
N = int(input())
q = deque(list(map(str, range(10))))

if N<10:
    print(q[N])
    exit(0)

cnt = 9
while q:
    c = q.popleft()
    for i in range(10):
        if int(c[-1]) <= i: break
        q.append(c+str(i))
        cnt += 1
        if cnt==N:
            print(q.pop())
            exit(0)
print(-1)