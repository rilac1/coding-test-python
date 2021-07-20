# 설탕 배달
n = int(input())

ret = 0
while n%5 != 0:
    n -= 3
    ret += 1
    if n < 0:
        print(-1)
        exit(0)

print(ret + n//5)