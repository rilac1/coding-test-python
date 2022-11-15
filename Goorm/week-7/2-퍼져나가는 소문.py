N, M = int(input()), int(input())
relations = [tuple(map(int, input().split())) for _ in range(M)]

parent = list(range(N+1))

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    pa, pb = find(a), find(b)
    if pa > pb:
        parent[pa] = pb
    elif pa < pb:
        parent[pa] = pb

for relation in relations:
    union(relation[0], relation[1])

for i in range(1, N+1):
    find(i)

print(parent.count(find(1)))
