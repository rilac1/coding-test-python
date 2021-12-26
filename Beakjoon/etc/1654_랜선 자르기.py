# 랜선 자르기
import sys
input = sys.stdin.readline
M,N = map(int, input().split())
cable = [int(input()) for _ in range(M)]

l,r = 1, max(cable)
while l<=r:
    leng = (l+r)//2
    cnt = 0
    for c in cable: cnt += c//leng
    if cnt<N: r = leng-1
    elif cnt>=N: l = leng+1
print(r)