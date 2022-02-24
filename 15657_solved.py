from select import select


N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))

selected = []
def dfs(n):
    if len(selected)==M:
        print(*selected)
        return
    for i in range(n,N):
        selected.append(arr[i])
        dfs(i)
        selected.pop()
dfs(0)