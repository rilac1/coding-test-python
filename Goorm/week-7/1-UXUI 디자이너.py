N, M = map(int, input().split())
event_count = [0] * (N+1)

for _ in range(M):
    for event in list(map(int, input().split()))[1:]:
        event_count[event] += 1

ans = []
max_count = max(event_count)
for i in range(1, N+1):
    if max_count == event_count[i]:
        ans.append(i)
print(*ans[::-1])
