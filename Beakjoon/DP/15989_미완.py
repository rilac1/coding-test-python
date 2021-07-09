# 1,2,3 더하기 4
import sys
input = sys.stdin.readline

T = int(input())
arr = []
for i in range(T):
    arr.append(int(input()))

def dfs(n, a):
    if a==n:
        return a
    return dfs(n, a+1)