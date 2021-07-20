# 멀티탭 스케줄링
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
order = list(map(int, input().split()))

tabs = []
def unplug(index):
    remain = order[(index+1):]
    check = []
    for i, v in enumerate(tabs):
        if v not in remain:
            return i
        check.append(remain.index(v))
    return check.index(max(check))

cnt = 0
for i in order:
    if i not in tabs:
        tabs.append(i)
        cnt += 1
    if cnt == N:
        break

ret = 0
for i, v in enumerate(order):
    if i < cnt:
        continue
    if v not in tabs:
        tabs[unplug(i)] = v
        ret += 1

print(ret)