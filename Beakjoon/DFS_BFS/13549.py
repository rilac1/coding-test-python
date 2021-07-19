# 숨바꼭질 3
# dijstra
import heapq
MAX = 100000
N, K = map(int, input().split())

heap = []
table = [1e9] * (MAX+1)
heapq.heappush(heap, (0, N))

while heap:
    dis, loc = heapq.heappop(heap)
    if not 0<= loc <=MAX:
        continue
    if dis<table[loc]:
        table[loc] = dis
        heapq.heappush(heap, (dis, loc*2))
        heapq.heappush(heap, (dis+1, loc+1))
        heapq.heappush(heap, (dis+1, loc-1))

print(table[K])