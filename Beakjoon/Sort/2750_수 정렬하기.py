# 수 정렬하기
import sys, heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    heapq.heappush(h, int(input()))

while h:
    print(heapq.heappop(h))