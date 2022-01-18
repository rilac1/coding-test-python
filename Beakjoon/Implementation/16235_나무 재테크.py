# 나무 재테크
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int, input().split())

tree = [[deque() for _ in range(N)] for _ in range(N)]
nourishment = [[5]*N for _ in range(N)]

A = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    x,y,z = map(int, input().split())
    tree[x-1][y-1].append(z)

def spring_summer():
    breed = []
    for i in range(N):
        for j in range(N):
            for n in range(len(tree[i][j])):
                if tree[i][j][n]<=nourishment[i][j]:
                    nourishment[i][j] -= tree[i][j][n]
                    tree[i][j][n] += 1
                    if tree[i][j][n] % 5 == 0:
                        breed.append((i,j))
                else:
                    for _ in range(n,len(tree[i][j])):
                        nourishment[i][j] += tree[i][j].pop()//2
                    break
    fall(breed)

def fall(breed):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for x,y in breed:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                tree[nx][ny].appendleft(1)
    winter()

def winter():
    for i in range(N):
        for j in range(N):
            nourishment[i][j] += A[i][j]

for _ in range(K):
    spring_summer()

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)