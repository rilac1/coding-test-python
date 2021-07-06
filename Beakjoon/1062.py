# 가르침
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = [[] for _ in range(N)]
alphabet = set()
for i in range(N):
    temp = (list(input().strip()))
    temp = temp[4:-4]
    words[i] = temp
    alphabet.update(temp)

if K<5:
    print(0)
    exit(0)

default = ['a','c','n','t','i']
alphabet = list(alphabet - set(default))
alphabet = list(alphabet)
print(alphabet)
learn = []

def check(l):
    ret = 0
    for w in words:
        ret += 1
        for a in w:
            if a not in l:
                ret -= 1
                break
    return ret

def back(i):
    global maxV
    if len(learn) == K-5:
        maxV = max(maxV, check(default+learn))
        return
    learn.append(alphabet[i])
    back(i+1)
    learn.pop(0)

maxV = 0
back(0)
print(maxV)
