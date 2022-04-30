N = int(input())

def isValid(select):
    n = len(select)
    for length in range(n//2+1):
        for l in range(n-length-1):
            if select[l:l+length]==select[l+length:l+length<<1]:
                return False
    return True

select = []
def back(n):
    global ans, N
    if not isValid(select): return

    if len(select)==N:
        for s in select: print(s,end='')
        print()
        exit(0)

    for i in range(1,4):
        if i!=n:
            select.append(i)
            back(i)
            select.pop()
back(0)