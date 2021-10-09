# 백터 매칭
import sys, math
input = sys.stdin.readline

def cal(a):
    if a < len(point)-1:
        for i in range(a+1,len(point)):
            x,y =  point[a], point[i]
            dist[a].append(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2))
        return cal(a+1)

def dfs(a):
    global ret
    if a<len(dist[a])-1:
        for i in range(a+1, len(dist[a])):
            ret += dist

T = int(input())
for _ in range(T):
    N = int(input())
    point = [tuple(map(int,input().split())) for _ in range(N)]
    dist = [[] for _ in range(N)]
    cal(0)

    for i in dist: print(i)
    