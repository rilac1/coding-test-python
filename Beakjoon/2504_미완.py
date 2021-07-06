# 괄호의 값
# 구현
import sys
input = sys.stdin.readline
arr = list(input())

inb = ['(', '[']
outb = [')', ']']
value = [2,3]
ret = 0

stack = []
op = []
for i in arr:
    if i in outb:
        idx = outb.index(i)
        if not stack or not inb[idx] == stack.pop():
            print(0)
            exit()
        temp = value[idx]
        if stack:
            if stack[-1] == '(':
                temp *=2
            else:
                temp *=3
        ret += temp
    else:
        stack.append(i)
print(ret)