import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = [set(input().rstrip()) for _ in range(N)]
s = ['a','n','t','i','c']
if K<5:
    print(0)
    exit(0)

bm={}
for w in words:
    for a in w:
        if a not in s: bm[a]=0
l = list(bm.keys())
if len(l)<K-5: 
    print(N)
    exit(0)
for i in s: bm[i]=1

def find():
    n=0
    for w in words:
        flag = True
        for a in w:
            if bm[a]==0:
                flag = False
                break
        if flag: n+=1
    return n

def back(left):
    global ans, k
    if k==K-5:
        ans = max(ans, find())
        return
    for i in range(left,len(l)):
        k+=1
        bm[l[i]]=1
        back(left+1)
        bm[l[i]]=0
        k-=1

ans,k = 0,0
back(0)
print(ans)