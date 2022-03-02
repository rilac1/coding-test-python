# 비밀번호 찾기
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
d = {}
for _ in range(N):
    site, password = input().rstrip().split()
    d[site] = password
for _ in range(M):
    print(d[input().strip()])