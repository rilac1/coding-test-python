# 가르침
# 백트래킹
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

if len(alphabet) <= K-5:
    print(len(words))
    exit(0)

learn = []
visited = [False] * len(alphabet)

def check(l):
    ret = 0
    for w in words:
        ret += 1
        for a in w:
            if a not in l:
                ret -= 1
                break
    return ret

def back(left):
    global maxV
    if len(learn) == K-5:
        maxV = max(maxV, check(default+learn))
        return
    for i in range(left, len(alphabet)):
        if not visited[i]:
            visited[i] = True
            learn.append(alphabet[i])
            back(i)
            learn.pop()
            visited[i] = False

maxV = 0
back(0)
print(maxV)