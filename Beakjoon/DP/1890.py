# 점프
import sys
input = sys.stdin.readline

N=int(input())
table = [[] for _ in range(N)]
for i in range(N):
    table[i] = list(map(int, input().split()))

# dp = [[True]*N for _ in range(N)]
ret = 0
def dfs(x, y):
    global ret
    if x>=N or y>=N:
        return False
    if table[x][y] == 0:
        return True

    n = table[x][y]
    if dfs(x+n, y) or dfs(x, y+n):
        table[x][y] = 0
        ret += 1

dfs(0,0)
print(ret)