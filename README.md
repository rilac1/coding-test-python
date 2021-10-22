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
def perm(n, r):
    if len(picked) == r:
        print(picked)
        return

    for i in range(len):
        if not visited[i]:
            picked.append(arr[i])   # 변화
            visited[i] = True
            perm(n, r)              # 재귀호출
            visited[i] = False
            picked.pop()            # 복원
```

## Combination (<sub>n</sub>C<sub>r</sub>)
```python
# 조합의 경우 visited가 필요없음
picked = []
def comb(n, r, left):
    if len(picked) == r:
        print(picked)
        return

    for i in range(left, n):        # left ~ n까지만 탐색
        picked.append(arr[i])       # 변화
        comb(n, r, i)               # 재귀호출 (마지막에 넣었던 index가 left가 된다.)
        picked.pop()                # 복원
```

## Dijkstra
```python
import heapq
def dijkstra(a):
    h = [(0,a)]
    distance = [1e9]*(V+1)
    while h:
        dis,b = heapq.heappop(h)
        if dis<distance[b]:
            distance[b] = dis
            for i,d in graph[b]:
                heapq.heappush(h, ((d+dis,i)))
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