# 최소 힙
import sys, heapq
input = sys.stdin.readline
N = int(input())
c = [int(input()) for _ in range(N)]

h = []
for i in c:
    if i: heapq.heappush(h, i)
    elif h: print(heapq.heappop(h))
    else: print(0)