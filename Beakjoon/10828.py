import sys
input = sys.stdin.readline
N = int(input())
cmd = []
for _ in range(N):
    command, val = input().split()
    cmd.append((command, int(val)))
print(cmd)
