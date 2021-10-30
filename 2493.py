import heapq
n = int(input())
tower = [0]+list(map(int, input().split()))
ans = [0]*(n+1)

stack = []
maxStack=0
for i in range(n+1):
    if stack:
        if tower[i]>maxStack:
            ...