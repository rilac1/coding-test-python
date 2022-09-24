from collections import deque

def solution(n, m, x, y, r, c, k):
    results = []
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    char = ['u', 'r', 'd', 'l']

    q = deque([(x, y, '')])
    for _ in range(k):
        for _ in range(len(q)):
            x, y, string = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 1 <= nx <= n and 1 <= ny <= m:
                    q.append((nx,ny,string+char[i]))

    while q:
        x, y, string = q.popleft()
        if x == r and y == c:
            results.append(string)

    if not results:
        return 'impossible'
    results.sort()
    return results[0]

print(solution(3,4,2,3,3,1,5))