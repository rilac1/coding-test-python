# 연산자 끼워넣기
# 트루트포스
# 시간초과... ㅠㅠ
import itertools

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

maxV = 0
minV = 1e9

def back(x, y, index):
    if index == n-1:
        maxV = max(maxV, x)
        minV = min(minV, x) 

    num = n[index]
    x += num
    back(x, index+1)

back(a[0], 1)


print(maxV)
print(minV)