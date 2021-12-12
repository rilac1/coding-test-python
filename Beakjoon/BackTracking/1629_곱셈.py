# 곱셈
def p(n):
    if n==1: return A%C
    else:
        t = p(n//2)
        if n%2: return t*t*A%C
        else: return t*t%C
A,B,C = map(int, input().split())
print(p(B))