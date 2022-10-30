from collections import deque

N = int(input())
dp = deque([0, 0, 1])

for i in range(3, N+1):
    dp.append((2*(i-1) + 1) * dp[-1] + dp[-2])
    dp.popleft()

print(dp[-1] % 100000007)
