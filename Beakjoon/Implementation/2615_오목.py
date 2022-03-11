# 오목
import copy
originalBoard = [list(map(int,input().split())) for _ in range(19)]
dx = [1,0,1,1]
dy = [0,1,1,-1]

def dfs(x,y,n):
    global board, d, rock
    nx = x+dx[d]
    ny = y+dy[d]

    if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==rock:
        board[nx][ny] = 0
        dfs(nx,ny,n+1)

    elif n==5:
        print(rock)
        if d==3: print(x+1,y+1)
        else: print(x-4*dx[d]+1, y-4*dy[d]+1)
        exit(0)
        
for d in range(4):
    board = copy.deepcopy(originalBoard)
    for i in range(19):
        for j in range(19):
            for rock in [1,2]:
                if board[i][j]==rock:
                    board[i][j] = 0
                    dfs(i,j,1)
print(0)