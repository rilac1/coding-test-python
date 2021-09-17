# 리모컨
nums = [1]*10
N, M = input(), int(input())
if not M:
    print(len(N))
    exit(0)
for i in map(int, (input().split())): nums[i] = 0

direction = 0
ch = []
for i in N:
    if nums[i]:
        ch.append(i)
    else:
        if direction==0:
            for j in range(5):
                ...