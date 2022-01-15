# CCW
P = [tuple(map(int, input().split())) for _ in range(3)]
x, y = [i[0]for i in P], [i[1]for i in P]
r = (x[0]*y[1] + x[1]*y[2] + x[2]*y[0])\
    - (x[1]*y[0] + x[2]*y[1] + x[0]*y[2])
if r>0: print(1)
elif r<0: print(-1)
else: print(0)