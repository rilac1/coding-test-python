import sys
input = sys.stdin.readline
N, M = map(int, input().split())
temp=list(map(int, input().split()))
if temp[0]: truth = temp[1:]
party=list(map(int, input().split())[1:] for _ in range(M))
if not temp[0]: 
    print(M)
    exit(0)

parent = list(range(N))
for p in party:
    for i in p:
