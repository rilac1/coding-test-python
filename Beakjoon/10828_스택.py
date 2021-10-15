# 스택
import sys
input = sys.stdin.readline
N = int(input())
cmd = [input().split() for _ in range(N)]
stack = []
for c in cmd:
    if len(c)==2: stack.append(int(c[1]))
    elif c[0]=='pop': 
        if stack: print(stack.pop())
        else: print(-1)
    elif c[0]=='size': print(len(stack))
    elif c[0]=='empty': print(int(len(stack)==0))
    elif c[0]=='top':
        if stack: print(stack[-1])
        else: print(-1)