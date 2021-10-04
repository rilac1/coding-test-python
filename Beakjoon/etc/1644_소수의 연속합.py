# 소수의 연속합
from collections import deque
N = int(input())
if N==1: 
    print(0)
    exit(0)

check = [True]*(N+1)
check[1]=False
prime = []
for n in range(1,N+1):
    if not check[n]: continue
    prime.append(n)
    i=2
    while i*n<=N:
        check[i*n]=False
        i+=1

q = deque([prime[0]])
cnt,q_sum,i = 0,prime[0],1
while q:
    if q_sum<N:
        if i==len(prime): break
        q.append(prime[i])
        q_sum += prime[i]
        i += 1
    else:
        if q_sum==N: cnt += 1
        q_sum -= q.popleft()
print(cnt)