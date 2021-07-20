import sys
input = sys.stdin.readline
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

def dfs(s, n):
    global ret
    global last
    if not 0<=s<=M:
        return
    if n==N:
        ret = max(ret, s)
        last = True
        return
    dfs(s+V[n], n+1)
    dfs(s-V[n], n+1)

ret = 0
last = False
dfs(S, 0)
if last:
    print(ret)