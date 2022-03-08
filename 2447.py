N = int(input())

def dfs(n,col,row):
    if n==1:
        if col==1 and row==1: print(' ', end='')
        else: print('*',end='')
        return

    n //= 3
    for i in range(3):
        for j in range(3):
            dfs(n,col+i,row+j)
    print()

dfs(N,0,0)