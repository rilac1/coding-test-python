import sys
input = sys.stdin.readline

T = int(input())
ret = []

for _ in range(T):
	N, M = map(int, input().split())
	queue = list(map(int, input().split()))
	for i in range(N):
		x = queue[i]
		queue[i] = (x, i)
	
	n = 1
	while queue:
		high, _ = max(queue)
		x, i = queue.pop(0)
		if x == high:
			if i==M:
				ret.append(n)
				break
			else:
				n += 1
		else:
			queue.append((x,i))

for i in ret:
	print(i)
