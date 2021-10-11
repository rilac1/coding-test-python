# 가운데를 말해요
## Hint...
import sys, heapq
input = sys.stdin.readline

N = int(input())
left,right = [], []
mid = int(input())
print(mid)

for i in range(0, N-1):
    x = int(input())
    if x < mid:
        heapq.heappush(left,-x)
        heapq.heappush(right,mid)
    else:
        heapq.heappush(left,-mid)
        heapq.heappush(right, x)
    if i%2==0:
        mid = -heapq.heappop(left)
    else:
        mid = heapq.heappop(right)
    print(mid)