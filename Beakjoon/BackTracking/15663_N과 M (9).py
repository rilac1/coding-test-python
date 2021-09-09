# N과 M (9)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))

picked = []
visited = [False]*N
def perm(n,r):
    if len(picked) == r:
        for i in picked:
            print(i, end = ' ')
        print()
        return
    temp = 0
    for i in range(n):
        if not visited[i] and temp!=num[i]:
            temp = num[i]
            picked.append(num[i])
            visited[i] = True
            perm(n,r)
            visited[i] = False
            picked.pop()

num.sort()
perm(N,M)