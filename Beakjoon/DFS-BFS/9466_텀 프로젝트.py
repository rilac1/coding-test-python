# 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x):
    visited[x] = True
    ring.append(x)
    if visited[next[x]]:
        if next[x] in ring: 
            return len(ring) - ring.index(next[x])
        else: 
            return 0
    return dfs(next[x])
    
T = int(input())
for _ in range(T):
    ret = 0
    n = int(input())
    next = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    for s in range(1,n+1):
        if not visited[s]:
            ring = [] 
            ret += dfs(s)
    print(n-ret)