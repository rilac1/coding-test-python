# ATM
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

time = 0
ret = 0
for i in arr:
    time += i
    ret += time
print (ret)