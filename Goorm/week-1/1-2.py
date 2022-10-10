import sys
input = sys.stdin.readline

n, s = input().split()
names = [input().rstrip() for _ in range(int(n))]

ans = 0
for name in names:
    ans += int(s in name)
print(ans)
