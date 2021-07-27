# 수들의 합
S = int(input())

cnt = 0
start = 0
while start<S:
    cnt += 1
    start += cnt
if start > S:
    cnt -= 1

print(cnt)