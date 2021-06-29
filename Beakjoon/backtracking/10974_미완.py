# 모든 순열
n = int(input())
arr = range(1,n+1)

def backtracking(cnt, idx):
    if (cnt==m):
        return
    for i in range(visited):
        if not visited[i]:
            visited[i] = True
            backtracking(cnt+1, i)
            visited[i] = False
