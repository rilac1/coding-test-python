# N과 M (5)
N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
selected = []
visited = [False]*N

def dfs():
    if len(selected)==M:
        print(*selected)
        return
    for i in range(N):
        if not visited[i]:
            selected.append(arr[i])
            visited[i] = True
            dfs()
            visited[i] = False
            selected.pop()
dfs()