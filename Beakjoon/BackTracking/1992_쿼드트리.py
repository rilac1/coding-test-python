# 쿼드트리
import sys
input = sys.stdin.readline
N = int(input())
bits = [input().rstrip() for _ in range(N)]

nx,ny = [0,0,1,1],[0,1,0,1]
def last(n,a,b):
    n >>=1
    if (n==0): return bits[a][b]
    temp = ""
    for i in range(4): temp += last(n, a+nx[i]*n, b+ny[i]*n)
    if '(' not in temp:
        if '0' not in temp: return '1'
        elif '1' not in temp: return '0'
    return '('+temp+')'
print(last(N,0,0))