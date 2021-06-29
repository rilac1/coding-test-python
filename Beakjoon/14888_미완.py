import itertools

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
operation = []
for i, x in enumerate(o):
    while x>0:
        operation.append(i)
        x -= 1

maxV = 0
minV = 1e9

def calculate(a,op,b):
    if op==0:
        return a+b
    elif op==1:
        return a-b
    elif op==2:
        return a*b
    elif op==3:
        if (a >= 0 and b>0) or (a<=0 and b<0) :
            return a//b
        elif a<0:
            return -(-a//b)
        elif b<0:
            return -(a//-b)


temp = a.pop(0)
for perm in itertools.permutations(operation):
    x = temp
    for i in range(n-1):
        x = calculate(x, perm[i], a[i])
    maxV = max(maxV, x)
    minV = min(minV, x)

print(maxV)
print(minV)