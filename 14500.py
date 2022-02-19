import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx,dy = [1,0], [0,1]
ans = 0
def dfs(x, y, val, cnt):
    global ans

    visited[x][y] = True
    val += graph[x][y]
    cnt += 1

    if cnt==4: 
        print_check()
        ans = max(ans, val)
    elif cnt==2:
        

    else:
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny]:
                    dfs(nx,ny,val,cnt)
        
    visited[x][y] = False
    return

for i in range(N):
    for j in range(M):
        dfs(i,j,0,0)
print(ans)


def print_check():
    for v1 in visited:
        for v2 in v1: 
            print(int(v2), end =' ')
        print()
    print()