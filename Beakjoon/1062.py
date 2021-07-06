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
    alphabet.add(temp)

if K<5:
    print(0)
    exit(0)
learn = ['a','c','n','t','i']

print(alphabet)
