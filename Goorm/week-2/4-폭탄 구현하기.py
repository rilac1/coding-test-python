import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
for _ in range(k):
    a, b = map(int, input().split())
    conditions = [
        0 < a <= n and 0 < b <= n,
        a+1 <= n,
        b+1 <= n,
        a-1 > 0,
        b-1 > 0
    ]
    ans += sum(map(int, conditions))
print(ans)
