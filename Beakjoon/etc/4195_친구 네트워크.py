# 친구 네트워크
## Union Find
import sys
input = sys.stdin.readline
F = int(input())

def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x
        ret[x] += ret[y]

for _ in range(F):
    N = int(input())
    parent = {}
    ret = {}
    for _ in range(N):
        a,b = input().split()
        if a in parent:
            if b in parent:
                union(a,b)
            else:
                parent[b] = find(a)
                ret[parent[b]] += 1
        else:
            if b in parent:
                parent[a] = find(b)
                ret[parent[a]] += 1
            else:
                parent[a], parent[b] = a,a
                ret[a]=2
        print(ret[parent[a]])
