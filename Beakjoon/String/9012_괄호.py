# 괄호
from inspect import stack
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    flag = True
    vps = input().rstrip()
    s = []
    for v in vps:
        if v==')':
            if s:
                if s.pop()=='(': continue
            flag = False
            break
        else:
            s.append(v)
    if s or not flag: print('NO')
    else: print('YES')