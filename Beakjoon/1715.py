# 카드 정렬하기
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
ret = 0
while len(heap)>1:
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, temp)
    ret+=temp
    
print(ret)