# 수 정렬하기 3
import sys
input = sys.stdin.readline
N = int(input())

data = {}
for _ in range(N):
    a = int(input())
    if a in data: data[a] += 1
    else: data[a] = 1
data = sorted(data.items())
for num, i in data:
    for _ in range(i):
        print(num)