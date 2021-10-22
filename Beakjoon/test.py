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
        order[Y].append(X)
    W = int(input())
    