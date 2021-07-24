# 피보나치 함수
import sys
input = sys.stdin.readline

T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))
dp0 = [1,0]
dp1 = [0,1]

for i in range(2, 41):
    dp0.append(dp0[i-1]+ dp0[i-2])
    dp1.append(dp1[i-1]+ dp1[i-2])

for n in N:
    print(dp0[n], dp1[n])
