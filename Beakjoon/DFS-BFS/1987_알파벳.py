# 알파벳
## 시간초과(pypy3)
## 람다식을 활용한 알파벳 스트링 입력받기
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
print(board)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [False]*26

def dfs(x,y,count):
    global ret
    ret = max(count, ret)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<R and 0<=ny<C and not visited[board[nx][ny]]:
            visited[board[nx][ny]] = True
            dfs(nx,ny,count+1)
            visited[board[nx][ny]] = False

ret = 0
visited[board[0][0]] = True
dfs(0,0,1)
print(ret)