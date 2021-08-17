# 전화번호 목록
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    number = [list(map(int, input().split())) for _ in range(n)]
    