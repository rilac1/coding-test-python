# A->B
a, b = map(int, input().split())

def bfs(temp, n):
    if temp==b:
        print(n)
        exit(0)
    elif temp>b:
        return
    bfs(temp*2, n+1)
    bfs(temp*10+1, n+1)

bfs(a, 1)
print(-1)