from collections import deque
gear = [deque(map(int,input())) for _ in range(4)]
K = int(input())
order = [tuple(map(int,input().split())) for _ in range(K)]

def rotate():
    for i in range(4):
        if direction[i]==1:
            gear[i].appendleft(gear[i].pop())
        elif direction==-1:
            gear[i].append(gear[i].popleft)

def check(i, n):
    next = i+n
    if 0<=next<4:
        if n==1:
            if gear[i][2]==gear[next][6]: return
        else:
            if gear[i][6]==gear[next][2]: return
        direction[next] = -direction[i]
        check(next,n)

for i, dir in order:
    i-=1
    direction = [0]*4
    direction[i] = dir
    check(i, -1)
    check(i, 1)
    rotate()
    for t in gear: print(*t)

ans = 0
for i in range(4):
    ans += gear[i][0]*(1<<i)
print(ans)