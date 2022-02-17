N,M = map(int, input().split())
graph = [list(map(int,input().split())) for  _ in range(N)]



cctv = []
for i in range(N):
    for j in range(M):
        if 0<graph[i][j]<6: cctv.append((i,j,graph[i][j]))

