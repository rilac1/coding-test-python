# ACM Craft
## 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    degree = [0]*(N+1)
    order = [[] for _ in range(N+1)]
    for _ in range(K):
        X,Y = map(int, input().split())
        degree[Y] += 1
        order[X].append(Y)
    W = int(input())

    dp = [0]*(N+1)
    q = deque()
    for i in range(1,N+1):
        if degree[i]==0:
            deque.append(q, i)
            dp[i] = D[i]

    while q:
        time = 0
        x = deque.popleft(q)
        for y in order[x]:
            degree[y] -= 1
            dp[y] = max(dp[y], dp[x]+D[y])
            if degree[y]==0:
                deque.append(q, y)
    print(dp[W])