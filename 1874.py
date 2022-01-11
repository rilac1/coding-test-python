import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
answer = []
cnt = 1
for a in arr:
    while cnt<=a:
        answer.append('+')
        stack.append(cnt)
        cnt += 1
    if stack[-1] == a:
        answer.append('-')
        stack.pop()
    else:
        print('NO')
        exit(0)

for ans in answer: print(ans)