# 스타트와 링크
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

def dfs(left, cnt):
    global ans
    if cnt == N>>1:
        ans = min(ans, cal(mask))
        return

    for i in range(left, N):
        mask[i] = True
        dfs(i+1, cnt+1)
        mask[i] = False

def cal(mask):
    a, b = [], []
    for i in range(N):
        if mask[i]: a.append(i)
        else: b.append(i)
    
    asum, bsum = 0,0
    for i in range(N>>1):
        for j in range(i+1,N>>1):
            asum += graph[a[i]][a[j]] + graph[a[j]][a[i]]
            bsum += graph[b[i]][b[j]] + graph[b[j]][b[i]]

    return abs(asum-bsum)

mask = [False]*N
mask[0] = True
ans = 1e9
dfs(1,1)
print(ans)