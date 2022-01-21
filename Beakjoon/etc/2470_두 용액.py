# 두 용액
## 투포인터
N = int(input())
liq = list(map(int, input().split()))
liq.sort()

v = 1e20
l, r = 0, N-1
while l<r:
    res = liq[l]+liq[r]
    if abs(res)<v:
        v = abs(res)
        ans = (liq[l],liq[r])
    if res>0: r -= 1
    else: l += 1
print(*ans)