# 연산자 끼워넣기
# 트루트포스
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

def cal(x, i):
    global maxV, minV
    if i == n:
        maxV = max(maxV, x)
        minV = min(minV, x)
        return

    if o[0]:
        o[0] -= 1
        cal(x + a[i], i+1)
        o[0] += 1
    if o[1]:
        o[1] -= 1
        cal(x - a[i], i+1)
        o[1] += 1
    if o[2]:
        o[2] -= 1
        cal(x * a[i], i+1)
        o[2] += 1
    if o[3]:
        o[3] -= 1
        cal(int(x / a[i]), i+1)
        o[3] += 1
maxV = -sys.maxsize - 1
minV = sys.maxsize
cal(a[0], 1)

print(maxV)
print(minV)