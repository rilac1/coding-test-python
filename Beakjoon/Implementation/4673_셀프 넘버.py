import heapq

h = []
for i in range(10000):
	sum = i
	while i:
		sum += i%10
		i //= 10
	heapq.heappush(h, sum)

n = 1
while n<=10000:
	temp = heapq.heappop(h)
	while n < temp:
		print(n)
		n+=1
	if n==temp:
		n+=1
