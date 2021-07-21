# 수들의 합
S = int(input())

cnt = 1
start = 0
while start<S:
    start += cnt
    cnt += 1

print(cnt)