# 약수 구하기
n, k = map(int, input().split())
divisor = []

temp = n**0.5
route = int(temp)
    
for i in range(1, route+1):
    if n % i == 0:
        a = n//i
        if a==i:
            divisor.append(a)
        else:
            divisor.append(a)
            divisor.append(i)

divisor.sort()
if len(divisor) > k:
    print(divisor[k-1])
else:
    print('0')