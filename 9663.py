N = int(input())

visited = [[False]*N for _ in range(N)]
cnt=0
def dfs(n):
    global cnt
    if n==8: cnt += 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                dfs(n+1)
                visited[i][j] = False
    return cnt
print(dfs(0))