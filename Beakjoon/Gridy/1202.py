# 보석 도둑
import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewel.sort()
bag.sort()
ret = 0
h = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        heapq.heappush(h, -jewel[0][1])
        heapq.heappop(jewel)
    if h:
        ret -= heapq.heappop(h)
print(ret)