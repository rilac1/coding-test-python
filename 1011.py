import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x,y = map(int,input().split())
    d = y-x
    
    i,cnt,n = 0,0,1
    while i<d:
        cnt += 1
        i += n
        if cnt%2==0: n+=1
    print(cnt)