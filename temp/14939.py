from copy import deepcopy


state = [list(input()) for _ in range(10)]
origGraph = [[False]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if state[i][j]=='O': origGraph[i][j] = True

dx = [0,0,1,0]
dy = [0,1,0,-1]

def click(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<10 and 0<=ny<10:
            graph[nx][ny] = not graph[nx][ny]

ans = 1e9
for mask in range(10):
    graph = deepcopy(origGraph)
    cnt = 0

    for i in range(1,10):
        for j in range(10):
            if graph[i-1][j]:
                cnt += 1
                click(i,j)

    for j in range(10):
        if graph[-1][j]: break
        else: ans = min(ans,cnt)

if ans<1e9: print(ans)
else: print(-1)

