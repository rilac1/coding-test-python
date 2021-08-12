# 핵심 개념들

## 에라토스테네스의 체
여러개의 소수를 판별해야 할 때에는 에라토스테네스의 체를 사용한다.

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