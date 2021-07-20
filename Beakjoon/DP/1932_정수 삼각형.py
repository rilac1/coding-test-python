# 정수 삼각형
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
for i in range(1,n):
    data[i][0] += data[i-1][0]
    for j in range(1,i):
        data[i][j] += max(data[i-1][j], data[i-1][j-1])
    data[i][i] += data[i-1][i-1]

print(max(data[n-1]))