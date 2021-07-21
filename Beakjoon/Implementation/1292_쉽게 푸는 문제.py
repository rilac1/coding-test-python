# 쉽게 푸는 문제
a, b = map(int,input().split())
arr = []
temp = 0
recent = 1
for _ in range(1,1001):
    arr.append(recent)
    temp += 1
    if temp == recent:
        temp = 0
        recent += 1
print(sum(arr[a-1:b]))