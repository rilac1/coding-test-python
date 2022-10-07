import heapq

N = int(input())
q = list(map(int, input().split()))
heapq.heapify(q)

for _ in range(N-1):
    for i in map(int, input().split()):
        if i > q[0]:
            heapq.heapreplace(q, i)

print(heapq.heappop(q))
