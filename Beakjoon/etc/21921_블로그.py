# 블로그
## 슬라이딩 윈도우
N, X = map(int,input().split())
arr = list(map(int,input().split()))
l, r = 0, X
window = sum(arr[l:r])
maxVal, cnt = window, 1

while r<N:
    window -= arr[l]
    window += arr[r]
    if window>maxVal:
        maxVal = window
        cnt = 1
    elif window==maxVal:
        cnt += 1
    l += 1
    r += 1

if maxVal == 0: print('SAD')
else:
    print(maxVal)
    print(cnt)