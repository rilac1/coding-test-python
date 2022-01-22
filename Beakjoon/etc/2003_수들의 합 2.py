# 수들의 합 2
## 투 포인터
N, M = map(int, input().split())
a = list(map(int, input().split()))

sum, cnt = a[0], 0
l,r = 0,0
while True:
    if sum>M:
        sum -= a[l]
        l += 1
    else:
        if sum==M: cnt+=1
        r += 1
        if r==N: break
        sum += a[r]
print(cnt)