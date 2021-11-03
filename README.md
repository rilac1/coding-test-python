# 새로 알게 된 개념들

## 에라토스테네스의 체
> 여러개의 소수를 판별해야 할 때에는 에라토스테네스의 체를 사용한다.  
- 2부터 N까지의 소수를 구한다고 했을 때 2부터 N까지 반복문을 돌면서 아래 과정을 반복하되, 지워진 수는 패스한다. `for n in range(2, N+1):`
- 지워지지 않은 수가 소수다.

## 백트래킹
> 모든 경우의 수를 탐색해야 할 때에는 재귀호출을 사용한다. (dfs)
## 깊은복사
```python
import copy
copy.deepcopy()
```

## 람다식을 활용한 알파벳 스트링 입력받기
```python
board = list(map(lambda x: ord(x)-65, input().rstrip()))
```
> ABCDE -> [0, 1, 2, 3, 4]

## 2차원 배열 한 줄로 입력받기
```python
N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
```

## RecursionError
> 최대 재귀 깊이 강제로 늘리기
```python
import sys
sys.setrecursionlimit(100000)
```

# My Library
## Permutation (<sub>n</sub>P<sub>r</sub>)
```python
visited = [False] * n
picked = []
def perm():
    global n,r
    if len(picked) == r:
        print(picked)
        return

    for i in range(len):
        if not visited[i]:
            picked.append(arr[i])  # 변화
            visited[i] = True
            perm()                 # 재귀호출
            visited[i] = False
            picked.pop()           # 복원
```

## Combination (<sub>n</sub>C<sub>r</sub>)
```python
# 조합의 경우 visited가 필요없음
picked = []
def comb(left):
    global n,r
    if len(picked) == r:
        print(picked)
        return

    for i in range(left, n):        # left ~ n까지만 탐색
        picked.append(arr[i])       # 변화
        comb(i+1)                   # 재귀호출 (마지막에 넣었던 index가 left가 된다.)
        picked.pop()                # 복원
```

## Dijkstra
```python
import heapq
def dijkstra(start):
    distance = [1e9]*(N+1)
    distance[start] = 0
    h = [(0, start)]
    while h:
        dist, now = heapq.heappop(h)
        if dist==distance[now]:
            for target,d in graph[now]:
                if dist+d < distance[target]:
                    distance[target] = dist+d
                    heapq.heappush(h, (dist+d, target))
    return distance
```

## Union_Find
```python
def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
```

## Eratosthenes' sieve
```python
prime = []
mask = [False]*(N+1)
for n in range(1,N+1):
    if mask[n]: 
        continue
    prime.append(n)
    i=2
    while i*n<=N:
        mask[i*n]=True
        i+=1
```

## Topology Sort
```python
from collections import deque
conditions = [[]]
degree = []

result = []
q = deque()
for i in range(N): 
    if degree[i]==0: deque.append(q, i)
while q:
    a = deque.popleft(q)
    result.append(a)
    for b in conditions[a]:
        degree[b] -= 1
        if degree[b]==0: deque.append(q, b)
```

## Segment Tree
```python
arr = []    # source array
tree = [0]*(4*N)

# initialize the tree
def init(start, end, node):
    if start==end: 
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1)
    return tree[node]

# sum of left~right
def t_sum(start, end, node):
    global left, right
    if start>right or end<left: return 0
    if start>=left and end<=right: return tree[node]
    mid = (start+end)//2
    return t_sum(start,mid,node*2) + t_sum(mid+1,end,node*2+1)

# change value
def update(start, end, node):
    global index, diff
    if start<=index<=end:
        tree[node] += diff
        if start!=end:
            mid = (start+end)//2
            update(start,mid,node*2)
            update(mid+1,end,node*2+1)

# main
init(0, N-1, 1)

left, right = a, b
print(t_sum(0, N-1, 1))

index, diff = i, x
update(0, N-1, 1)
```
> index가 1부터 시작시 `arr=[0]+[], init(1,N,1)`