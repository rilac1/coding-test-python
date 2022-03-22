# 키로거
import sys
from collections import deque
input = sys.stdin.readline
ans = []

for _ in range(int(input())):
    left = deque()
    right = deque()
    for s in input().rstrip():
        try:
            if s=='<': right.appendleft(left.pop())
            elif s=='>': left.append(right.popleft())
            elif s=='-': left.pop()
            else: left.append(s)
        except: ...
    ans.append("".join(left+right))

for a in ans: print(a)