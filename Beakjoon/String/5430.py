# AC
## R: 배열 뒤집기
## D: 첫 번째 숫자 버리기
import sys
input = sys.stdin.readline

T = int(input())
ret = []

for i in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    print(arr)
    
    isError = False
    for func in p:
        if func == 'R':
            arr.reverse()
        elif func == 'D':
            if not arr:
                isError = True
                break
            arr.pop(0)
    
    if isError:
        ret.append('error')
    else:
        ret.append(list(map(int, arr)))

for i in ret:
    print(i)
