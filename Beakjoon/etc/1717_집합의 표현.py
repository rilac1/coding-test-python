# 집합의 표현
## Union Find
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

parent = list(range(n+1))
def find(x):
    if x==parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x,y = find(x), find(y)
    if x!=y: parent[y] = x

for _ in range(m):
    o,a,b = map(int, input().split())
    if o: 
        if find(a)==find(b): print('yes')
        else: print('no')
    else: union(a,b)