N,M = map(int,input().split())
selected = []
visited = [False]*(N+1)
def dfs():
    if len(selected)==M:
        print(*selected)
        return
    for i in range(1,N+1):
        if not visited[i]:
            selected.append(i)
            visited[i]=True
            dfs()
            visited[i]=False
            selected.pop()
dfs()