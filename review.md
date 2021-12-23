## 분할정복
#### 쿼드트리
https://www.acmicpc.net/problem/1992
- 특이점: X
- 예외처리: X
- 유형분석: 분할정복은 가장 말단 케이스를 먼저 구현해놓고 차례차례 올라가는 것이 편한 것 같다.

#### 곱셈
https://www.acmicpc.net/problem/1629
- 특이점: 단순하게 풀면 시간초과 남
- 유형분석: 분할정복에서 동일한 연산 결과를 사용할 경우 미리 분할정복한 결과를 temp로 저장한다.
- 새로 알게된 점: `(n*n)%3 = (n%3)*(n%3)%3`

---
## DFS/BFS
#### 촌수계산
https://www.acmicpc.net/problem/2644
- 특이점: X
- 예외처리: X
- 느낀점: X

#### 스타트링크
https://www.acmicpc.net/problem/5014
- 특이점: X
- 유형분석: BFS를 할 때 큐에서 뺀 뒤에 방문 표시를 하게 되면 같은 정점이 동시에 큐에 들어간 뒤, 나온 뒤 그에 연결된 같은 정점을 중복해서 넣고, 그 정점들이 또 같은 정점을 중복해서 넣고... 하는 것이 반복되어 지수 시간 복잡도가 된다.

#### 안전영역
https://www.acmicpc.net/problem/2468
- 특이점: DFS와 전체탐색을 같이 해야함.
- 예외처리: 비가 안올 때를 생각해야함. 따라서 답은 무조건 1이상이 나와야 함. 
- 예외처리: sys.setrecursionlimit(100000)
- 새로 알게 된 점: 2차원 배열의 최댓값 (`m = max(map(max, graph))`)
---

## 이분탐색
#### 나무 자르기
https://www.acmicpc.net/problem/2805
