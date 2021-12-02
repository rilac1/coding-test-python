A,B,C = map(int, input().split())
r = [A%C]
for _ in range(B):
    A *= A
    t = A%C
    if t==0:
        print(0)
        exit(0)
    elif t==r[0]:
        print(r[B%len(r)])
        exit(0)
    else: r.append(t)
print(A%C)

# 2147483647 2147483647 2147483647