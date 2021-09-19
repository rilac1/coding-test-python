import sys
input=sys.stdin.readline
N=int(input())
arr=[int(input()) for _ in range(N)]

ret = 0
s_arr=sorted(arr)
i=0
while i<N:
    if arr[i]==s_arr[i]:
        i+=1
        continue
    target = s_arr[i]
    temp = arr[target]


print(ret)