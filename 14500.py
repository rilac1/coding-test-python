from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

ans = 0
q = deque([(0,0,0,0)])
while q:
    x,y,cnt,value = q.popleft()
    if cnt==4:
        ans = max(ans,value)
        continue
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            q.append((nx,ny,cnt+1, value+graph[x][y]))
        
print(ans)