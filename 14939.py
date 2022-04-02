from copy import deepcopy
state = [list(input()) for _ in range(10)]
graph = [[False]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if state[i][j]=='O': graph[i][j] = True

dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

def click(x,y):
    for i in range(5):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<10 and 0<=ny<10:
            graph[nx][ny] = not graph[nx][ny]

def dfs(n, cnt, graph):
    if n==10: return cnt
    if graph[0][n]:
        click(0,n)
        for i in range(1,10):
            for j in range(10):
                if graph[i-1][j]:
                    cnt += 1
                    click(i,j)
        dfs(n+1, cnt+1, deepcopy(graph))
        click(0,n)
    else: dfs(n+1, cnt, graph)
    
print(dfs(0,0,graph))