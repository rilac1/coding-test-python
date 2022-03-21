# 감시
from copy import deepcopy
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

cctvType = [
    [],
    [[0],[1],[2],[3]],
    [(0,2),(1,3)],
    [(0,1),(1,2),(2,3),(3,0)],
    [(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
]

class CCTV:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.dir = cctvType[type]

    def add(self, i):
        moving = []
        for d in self.dir[i]:
            moving.append((self.x,self.y,d))
        return moving
    
    def size(self):
        return len(self.dir)
    
def move(board,x,y,i):
    dx = [-1,0,1,0]
    dy = [ 0,1,0,-1]

    cnt = 0
    while True:
        x+=dx[i]
        y+=dy[i]
        if 0<=x<N and 0<=y<M and board[x][y]!=6:
            if board[x][y]==0:
                board[x][y] = -1
                cnt += 1
        else: return cnt

def dfs(n,left):
    global ans, cctvNUM, spot
    if n==cctvNUM:
        copiedGraph = deepcopy(graph)
        cnt = spot
        for m in moveQ:
            for x,y,d in m:
                cnt -= move(copiedGraph,x,y,d)
            ans = min(ans,cnt)
        return

    for i in range(left,cctvNUM):
        cctv = cctvList[i]
        for d in range(cctv.size()):
            moveQ.append(cctv.add(d))
            dfs(n+1,i+1)
            moveQ.pop()

cctvList = []
spot = 0
temp = []
for i in range(N):
    for j in range(M):
        t = graph[i][j]
        if t==0:
            spot += 1
        elif t==5:
            temp.append((i,j))
        elif t!=6:
            cctvList.append(CCTV(i,j,t))

cctvNUM = len(cctvList)

for x,y in temp:
    for i in range(4):
        spot -= move(graph,x,y,i)

moveQ = []
ans = spot
dfs(0,0)

print(ans)