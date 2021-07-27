# 두 포인터
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
for i in range(N):
    sum.append(num[i] + sum[i])

ret = 1e9
left, right = 0, 1

while left<N:
    if sum[right] - sum[left] >= S:
        ret = min(ret, right-left)
        left += 1
    else:
        if right<N:
            right += 1
        else:
            left += 1

if ret<1e9:
    if S==0:    
        print(1)
    else:    
        print(ret)
else:
    print(0)