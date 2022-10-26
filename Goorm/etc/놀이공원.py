for _ in range(int(input())):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    ans = 1e9
    for col in range(N-K+1):
        for row in range(N-K+1):
            result = 0
            for i in range(col, col+K):
                for j in range(row, row+K):
                    result += graph[i][j]
            ans = min(ans, result)

    print(ans)