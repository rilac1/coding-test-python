N = int(input())

def isValid(select):
    n = len(select)
    for length in range(1,n//2+1):
        for l in range(n-length-1):
            if select[l:l+length]==select[l+length:l+length<<1]:
                return False
    return True

select = [1]
def back():
    global ans, N
    if not isValid(select): return

    if len(select)==N:
        for s in select: print(s, end='')
        print()
        exit(0)

    for i in range(1,4):
        if i!=select[-1]:
            select.append(i)
            back()
            select.pop()
back()