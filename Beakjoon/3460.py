# 이진수
t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

for i in n:
    bin = []
    while i>1:
        bin.append(i%2)
        i = i >> 1
    bin.append(1)
    for j, x in enumerate(bin):
        if x==1:
            print(j, end= ' ')
    print()
