from math import ceil

N1, N2 = map(int, input().split())
D = int(input())

for i in range(D):
    if i % 2:
        amount = ceil(N2 / 2)
        N1 += amount
        N2 -= amount
    else:
        amount = ceil(N1/2)
        N1 -= amount
        N2 += amount

print(N1, N2)