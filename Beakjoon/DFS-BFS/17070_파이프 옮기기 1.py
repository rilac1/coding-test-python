# 파이프 옮기기 1
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

if graph[N-1][N-1]:
    print(0)
    exit(0)
    
tail,head = (1,1), (1,2)

dx = [[0,1],[1,1],[0,1,1]]
dy = [[1,1],[0,1],[1,0,1]]

def type(tail, head):
    if tail[0]==head[0]:
        return 0
    elif tail[1]==head[1]:
        return 1
    else:
        return 2

def dfs(tail,head):
    global cnt
    if head==(N-1,N-1):
        cnt += 1
        return

    t = type(tail, head)
    for i in range(len(dx[t])):
        x = head[0] + dx[t][i]
        y = head[1] + dy[t][i]
        if 0<=x<N and 0<=y<N and graph[x][y]==0:
            if i==len(dx[t])-1:
                if graph[x-1][y]==1 or graph[x][y-1]==1:
                    break
            dfs(head, (x,y))

cnt = 0
dfs((0,0),(0,1))
print(cnt)