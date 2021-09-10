import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = []
for _ in range(N):
    M, V = map(int, input().split())
    jewel.append((V, M))
bag = [int(input()) for _ in range(K)]

jewel.sort()
bag.sort()
ret = 0
while jewel and bag:
    v, m = jewel.pop()
    start, end = 0, len(bag)-1
    while start < end:
        mid = (start+end)//2
        if m == bag[mid]:
            start = end = mid
        elif m < bag[mid]:
            end = mid
        else:
            start = mid + 1
    if m <= bag[end]:
        ret += v
        bag.pop(end)

print(ret)