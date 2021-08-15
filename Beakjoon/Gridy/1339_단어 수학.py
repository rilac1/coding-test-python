import sys
input = sys.stdin.readline
N = int(input())
data = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(N)]

score = [0] * 26
for i in data:
	w = 1
	for j in reversed(i):
		score[j] += w
		w *= 10

score.sort(reverse=True)
ret = 0
for i in reversed(range(10)):
	ret += score.pop(0)*i

print(ret)
