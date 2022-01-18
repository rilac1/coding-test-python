import sys, heapq
input = sys.stdin.readline
N,M,K = map(int, input().split())

tree = []
dead = []
breed = []
nourishment = [[5]*N for _ in range(N)]

A = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    x,y,z = map(int, input().split())
    heapq.heappush(tree, (z,x-1,y-1))

def spring():
    grow = []
    while tree:
        t,x,y = heapq.heappop(tree)
        if nourishment[x][y]>=t:
            nourishment[x][y] -= t
            grow.append((t+1,x,y))
            if (t+1)%5==0:
                breed.append((x,y))
        else:
            dead.append((x,y,t//2))
    while grow:
        heapq.heappush(tree, grow.pop())

def summer():
    while dead:
        x,y,n = dead.pop()
        nourishment[x][y] += n

def fall():
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    while breed:
        x,y = breed.pop()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                heapq.heappush(tree, (1,nx,ny))

def winter():
    for i in range(N):
        for j in range(N):
            nourishment[i][j] += A[i][j]

for _ in range(K):
    spring()
    summer()
    fall()
    winter()
print(len(tree))