import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
N = int(input())
cmd = [tuple(input().split()) for _ in range(N)]

for i in range(N):
    c = cmd[i][0]
    try:
        if c=='L': right.append(left.pop())
        elif c=='D': left.append(right.pop())
        elif c=='B': left.pop()
        elif c=='P': left.append(cmd[i][1])
    except: ...

print("".join(left)+"".join(right[::-1]))