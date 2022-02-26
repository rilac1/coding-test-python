import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

d = [-1,0,1]
q = deque()
for i in range(3): q.append((graph[0][i], i))
for x in range(N):
    for _ in range(len(q)):
        score,y = q.popleft()
        for i in range(3):
            ny = y+d[i]
            if 0<=ny<3:
                q.append((score+graph[x][ny], ny))
ans = sorted(q)
print(ans[-1][0], ans[0][0])