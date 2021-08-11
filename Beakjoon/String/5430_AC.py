# AC
## R: 배열 뒤집기
## D: 첫 번째 숫자 버리기
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    if arr[0] == '':
        arr = []
    
    left = 0
    right = n-1
    reverse = False
    isError = False
    for func in p:
        if func == 'R':
            reverse = not reverse

        elif func == 'D':
            if right<left:
                isError = True
                break
            elif reverse:
                right-=1
            else:
                left+=1
    if isError:
        print('error')
    else:
        temp = arr[left:right+1]
        if reverse:
            temp.reverse()
        print('[' + ','.join(temp) + ']')
