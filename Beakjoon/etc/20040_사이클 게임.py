# 사이클 게임
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int,input().split())
action = [tuple(map(int, input().split())) for _ in range(m)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x, y = find(x), find(y)
    if x != y: 
        parent[y] = x
        return False
    else:
        return True

parent = list(range(0,n))
for i,(a,b) in enumerate(action):
    if union(a,b):
        print(i+1)
        break
else: print(0)