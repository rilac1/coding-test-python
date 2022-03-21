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
    global ans, blindSpot

    if n==len(cctvList):
        copiedGraph = deepcopy(graph)
        cnt = blindSpot
        for m in moveStack:
            for x,y,d in m:
                cnt -= move(copiedGraph,x,y,d)
        ans = min(ans,cnt)
        return

    for i in range(left, len(cctvList)):
        cctv = cctvList[i]
        for d in range(cctv.size()):
            moveStack.append(cctv.add(d))
            dfs(n+1,i+1)
            moveStack.pop()

blindSpot = 0
cctvList = []
cctvFives = []
for i in range(N):
    for j in range(M):
        t = graph[i][j]
        if t==0:
            blindSpot += 1
        elif t==5:
            cctvFives.append((i,j))
        elif t!=6:
            cctvList.append(CCTV(i,j,t))

# 5번 CCTV는 방향이 하나.
# 고로 탐색하지 않게 미리 그래프에 반영.
for x,y in cctvFives:
    for i in range(4):
        blindSpot -= move(graph,x,y,i)

moveStack = []
ans = blindSpot
dfs(0,0)

print(ans)