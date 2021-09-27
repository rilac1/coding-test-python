# 줄 세우기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
compare = [tuple(map(int, input().split())) for _ in range(M)]

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y: parent[y] = x

parent = list(range(N+1))
for a,b in compare: union(a,b)
group=[[] for _ in range(N+1)]
for i in range(N,0,-1): group[find(i)].append(i)
for g in group:
    for a in g:
        print(a,end=' ')
print()