# 전화번호 목록
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = [input().rstrip() for _ in range(N)]
    a.sort()
    b = True
    for i in range(N-1):
        if a[i]==a[i+1][:len(a[i])]: 
            b = False
            break
    if b: print('YES')
    else: print('NO')