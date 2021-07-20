# 뱀
n = int(input())
k = int(input())
data = [[0] * n for _ in range(n)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a-1][b-1] = 1

l = int(input())
for _ in range(l):
    temp = input().split()
    info.append((int(temp[0]), temp[1]))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

time, x, y = 0,0,0
cur = 1
body = []

while(True):
    # 이동
    body.append((x,y))
    x += dx[cur]
    y += dy[cur]
    time += 1

    # 회전
    if len(info)>0 and time == info[0][0]:
        t, d = info.pop(0)
        if d == 'L':
            cur -= 1
        elif d == 'D':
            cur += 1
        cur %= 4

    # 벽에 닿는지 or 몸에 닿는지
    if (x not in range(n) or y not in range(n) or (x,y) in body):
       print(time)
       break

    # 사과 있는지
    if (data[y][x] == 1):
        data[y][x] = 0
    else:
        body.pop(0)