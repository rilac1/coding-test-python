N = int(input())

def erase(x, y):
    i=1
    while x*i<=y:
        check[x*i]=False
        i+=1

check = [True]*(N+1)
check[1]=False
prime = []
for n in range(1,N+1):
    if not check[n]:   
        continue
    prime.append(n)
    if n==2 or n==3:
        erase(n,N)
    else:
        n*=n
        erase(n,N)

cnt = 0
a,b=0.0
temp = 0
while b<=len(prime):
    if a==b: 
        if prime[b] == N:
            cnt += 1
            a += 1
        elif prime[b] < N:
            b+=1
        else:
            break
    else:
        ...
        
