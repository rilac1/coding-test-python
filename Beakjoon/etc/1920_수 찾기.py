# 수 찾기
N = int(input())
a = sorted(map(int, input().split()))
M = int(input())
r = list(map(int, input().split()))

def bisect(l,r):
    global t
    while l<r:
        m = (l+r)//2
        if t<a[m]: r = m-1
        elif t>a[m]: l = m+1
        else: return 1
    return 0

for t in r: print(bisect(0, N))