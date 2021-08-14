import sys
input = sys.stdin.readline
N = int(input())
stack = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(N)]

pro = [[] for _ in range(10)]
for i in range(10):
    for j in range(N):
        if stack[j]:
            pro[i].append(stack[j].pop())
    i += 1

for i in reversed(range(10)):
    if not pro[i]:
        continue
    for i in