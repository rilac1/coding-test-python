# 수 정렬하기 2
## 병합정렬
import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

def merge(a):
    mid = len(a)//2
    if mid==0: 
        return a
    l,r = merge(a[:mid]), merge(a[mid:])
    res = []
    i,j = 0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    res+=l[i:]
    res+=r[j:]
    return res

for i in merge(arr): print(i)