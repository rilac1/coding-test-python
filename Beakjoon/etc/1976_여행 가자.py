# 여행 가자
## Union Find
N = int(input())
M = int(input())

def find(x):
    if x==parent[x]: return x
    return find(parent[x])

def union(x,y):
    x,y = find(x), find(y)
    if x != y: parent[y] = x

parent = list(range(N))
for i in range(N):
    for j,v in enumerate(map(int, input().split())):
        if v: union(i,j)
plan = list(map(int,input().split()))

final = find(plan[0]-1)
for p in plan:
    if find(p-1) != final:
        print('NO')
        break
else: print('YES')