import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = [int(j) for j in input().rstrip()]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
complex = []

def dfs(a,b):
    global temp
    if graph[a][b]==0:
        return
    temp += 1
    graph[a][b] = 0
    for i in range(4):
        dfs(a+dx[i], b+dy[i])

for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            continue
        temp = 0
        dfs(i,j)
        complex.append(temp)

complex.sort()
print(len(complex))
for i in complex:
    print(i)