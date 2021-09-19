# 거짓말
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
temp=list(map(int, input().split()))
if temp[0]: truth = set(temp[1:])
party=list(set(list(map(int, input().split()))[1:]) for _ in range(M))
if not temp[0]: 
    print(M)
    exit(0)

i=0
visited = [False]*M
while i<M:
    if not visited[i] and not party[i].isdisjoint(truth):
        visited[i]=True
        truth.update(party[i])
        i=0
    else: i+=1

cnt=0
for p in party:
    if p.isdisjoint(truth): cnt += 1
print(cnt)