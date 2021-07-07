# 퇴사2
import sys
input = sys.stdin.readline
N = int(input())
table = [[] for _ in range(N+1)]

for i in range(1, N+1):
    t,p = map(int, input().split())
    table[i] = (t, p)
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):         # 손님종류 = 현재시간
    for j in range(1, N+1):
        ...