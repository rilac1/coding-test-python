# 회의실 배정
import sys
input = sys.stdin.readline
N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

schedule.sort(key=lambda a: a[0])
schedule.sort(key=lambda a: a[1])
last = 0
cnt = 0
for a, b in schedule:
    if a>=last:
        cnt += 1
        last = b
print(cnt)