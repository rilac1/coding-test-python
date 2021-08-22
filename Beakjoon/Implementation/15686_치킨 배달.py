# 치킨 배달
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

def checkDis(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

picked = []
ret = []
visited = [False] * len(chicken)
def dfs(left, M):
    if len(picked)==M:
        sum_dis = 0
        for h in house:
            mindis = 1e9
            for c in picked:
                mindis = min(mindis, checkDis(h,c))
            sum_dis += mindis
        ret.append(sum_dis)
        return
    
    for i in range(left, len(chicken)):
        if not visited[i]:
            picked.append(chicken[i])
            visited[i] = True
            dfs(i, M)
            visited[i] = False
            picked.pop()

dfs(0, M)
print(min(ret))