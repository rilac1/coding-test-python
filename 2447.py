N = int(input())

def dfs(n,col,row):
    if n==1:
        print('*',end='')
        if row==N-1: print()
        return

    n //= 3
    dfs(n,col,row)
    dfs(n,col,row+n)
    dfs(n,col,row+n+n)
    
    dfs(n,col+n,row)
    dfs(n,col+n,row+n+n)

    dfs(n,col+n+n,row)
    dfs(n,col+n+n,row+n)
    dfs(n,col+n+n,row+n+n)


dfs(N,0,0)