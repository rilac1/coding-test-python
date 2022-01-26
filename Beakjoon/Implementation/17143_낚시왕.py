# 낚시왕
import sys
from collections import deque
input = sys.stdin.readline
R,C,M = map(int, input().split())
dx, dy = [0,-1,1,0,0], [0,0,0,1,-1]
graph = [[0]*(C+1) for _ in range(R+1)]

class Shark:
    def __init__(self, r, c, speed, direction, size):
        self.x = r
        self.y = c
        self.s = speed
        self.d = direction
        self.z = size

    def isLive(self):
        return self.z==graph[self.x][self.y]

    def move(self):
        if self.isLive():
            nx, ny = self.x, self.y
            for _ in range(self.s):
                if self.d==1 and nx==1: self.d += 1
                elif self.d==2 and nx==R: self.d -= 1
                elif self.d == 3 and ny==C: self.d += 1
                elif self.d == 4 and ny==1: self.d -= 1

                nx += dx[self.d]
                ny += dy[self.d]

            if self.z > moved[nx][ny]:
                moved[nx][ny] = self.z
                self.x, self.y = nx, ny
                return True
        return False

q = deque([])
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    if d==1 or d==2: s %= (R-1)*2
    else: s %= (C-1)*2

    q.append(Shark(r,c,s,d,z))
    graph[r][c] = z

fisher = 0
ans = 0
while q and fisher<C:
    # 1
    fisher += 1

    # 2
    for i in range(1,R+1):
        if graph[i][fisher]:
            ans += graph[i][fisher]
            graph[i][fisher] = 0
            break
    
    # 3
    moved = [[0]*(C+1) for _ in range(R+1)]
    for _ in range(len(q)):
        shark = q.popleft()
        if shark.move(): q.append(shark)
    graph = moved
print(ans)