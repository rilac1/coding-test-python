
# 핵심 개념들

## 에라토스테네스의 체
> 여러개의 소수를 판별해야 할 때에는 에라토스테네스의 체를 사용한다.  
- 2부터 N까지의 소수를 구한다고 했을 때 2부터 N까지 반복문을 돌면서 아래 과정을 반복하되, 지워진 수는 패스한다. `for n in range(2, N+1):`
  - n이 2나 3일 때는 n의 배수를 모두 지운다. (2,3,4,6,9, ... )
  - 이후에는 n의 제곱부터 n의 배수를 지운다. (n<sup>2</sup> + i*n)
    - n이 5면 25부터 5의 배수가 지워짐 (25, 30, 35, 40, ...)
    - n이 7이면 49부터 7의 배수가 지워짐 (49, 56, 63, 70, ...)
- 지워지지 않은 수가 소수다.

## 백트래킹
모든 경우의 수를 탐색해야 할 때에는 재귀호출을 사용한다. (bfs)

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
graph = [list(map(int, input().split())) for _ in range(N)]
```

## RecursionError
> 최대 재귀 깊이 강제로 늘리기
```python
import sys
sys.setrecursionlimit(100000)
```