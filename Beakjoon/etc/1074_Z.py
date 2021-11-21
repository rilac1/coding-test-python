# Z
def Z(n,x,y,i):
    global r,c
    if n==0:
        if x==r and y==c: print(i)
    else:
        nx, ny = x+(1<<(n-1)), y+(1<<(n-1))
        if r<nx: nx = x
        else: i+=(1<<(n<<1))>>1
        if c<ny: ny = y
        else: i+=(1<<(n<<1))>>2
        Z(n-1,nx,ny,i)       
N, r, c = map(int,input().split())
Z(N,0,0,0)