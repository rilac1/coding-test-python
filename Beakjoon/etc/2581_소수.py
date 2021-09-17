# 소수
m = int(input())
n = int(input())
a = list(range(10001))
if m==1:
    m+=1

for i in a[2:]:
    if i == 0:
        continue
    temp = i*2
    while temp < 10001:
        a[temp] = 0
        temp += i

prime = []
for p in a[m:n+1]:
    if not p==0:
        prime.append(p)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])