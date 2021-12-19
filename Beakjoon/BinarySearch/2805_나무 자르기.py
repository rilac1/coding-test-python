# 나무 자르기
N,M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

l, r = 0, trees[0]
while l<=r:
    mid = (l+r)//2
    s = 0
    for t in trees:
        if t<=mid: break
        s += t-mid
    if s<M: r = mid-1
    else: l = mid+1
print(r)