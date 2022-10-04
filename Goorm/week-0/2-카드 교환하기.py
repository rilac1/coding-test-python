import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, M = map(int, input().split())
cards = [0] + list(map(int, input().split()))
parent = list(range(N+1))

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

for _ in range(M):
    u,v = map(int, input().split())
    union(u,v)

groups = {}
for i in range(1, len(parent)):
    p = find(i)
    if p in groups:
        groups[p].append(i)
    else:
        groups[p] = [i]

answer = 0
for group in groups.values():
    group_card = [cards[person] for person in group]
    group_card.sort()
    for i in range(len(group)):
        answer += abs(group[i] - group_card[i])

print(answer)
