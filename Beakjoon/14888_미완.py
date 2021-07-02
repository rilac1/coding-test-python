# 연산자 끼워넣기
# 트루트포스
import itertools

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

maxV = 0
minV = 1e9

def cal(x, i):
    if i == n-1:
        maxV = max(maxV, x)
        minV = min(minV, x)
        return x
    if o[0]>0:
        o[0] -= 1
        x = cal(x + a[i], i+1) - a[i]
        o[0] += 1
    if o[1]>0:
        o[1] -= 1
        x = cal(x - a[i], i+1) + a[i]
        o[1] = 1
    if o[2]>0:
        o[2] -= 1
        x = cal(x * a[i], i+1) // a[i]
        o[2] += 1
    if o[3]>0:
        o[3] -= 1
        x = cal (x // a[i], i+1) * a[i]
        o[3] += 1

cal(a[0], 1)
print(maxV)
print(minV)