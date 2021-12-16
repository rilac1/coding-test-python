# 나무 자르기
N,M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

def f(h):
    l = 0
    for t in trees: l+=(t-h)
    return l

h = 1
while True:
    s = f(h)
    if s<M: h<<=1
    elif s>M: h>>=1
    else: print(h)
