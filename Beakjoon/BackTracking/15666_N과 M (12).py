# N과 M (12)
N,M = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
selected = []
def dfs(left):
    if len(selected)==M:
        print(*selected)
        return
    for i in range(left, len(arr)):
        selected.append(arr[i])
        dfs(i)
        selected.pop()
dfs(0)