# N과 M (2)
N, M = map(int, input().split())
c = []

def comb(left):
    global N,M
    if len(c)==M: print(*c)
    else: 
        for i in range(left, N+1):
            c.append(i)
            comb(i+1)
            c.pop()
comb(1)