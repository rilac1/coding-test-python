# 구슬탈출 2
from collections import deque
N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
dx,dy = [-1,0,1,0], [0,1,0,-1]

def move(marble,d):
    (x,y),cnt = marble, 0
    while board[x+dx[d]][y+dy[d]]!='#' and board[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return (x,y),cnt

for i in range(1,N-1):
    for j in range(1,M-1):
        if board[i][j]=='R': 
            red = (i,j)
            board[i][j] = '.'
        elif board[i][j]=='B':
            blue = (i,j)
            board[i][j] = '.'
        elif board[i][j]=='O':
            hole = i,j

q = deque([(red,blue,1)])
while q:
    red,blue,cnt = q.popleft()
    for i in range(4):
        r, rcnt = move(red,i)
        b, bcnt = move(blue,i)
        if r==hole: 
            if b!=hole:
                print(cnt)
                exit(0)
        else:
            if r==b:
                if rcnt>bcnt:
                    r = r[0]-dx[i], r[1]-dy[i]
                else:
                    b = b[0]-dx[i], b[1]-dy[i]
            if b!=hole and cnt<10:
                q.append((r,b,cnt+1))
print(-1)