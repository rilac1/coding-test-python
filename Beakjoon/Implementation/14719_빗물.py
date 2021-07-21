# 빗물
# 구현
H, W = map(int, input().split())
block = list(map(int, input().split()))

ret = 0
for h in range(H+1):
    temp = 0
    wall = False
    for w in range(W):
        if block[w] >= h:
            if wall:
                ret += temp
                temp = 0
            else:
                wall = True
        elif wall:
            temp += 1

print(ret)