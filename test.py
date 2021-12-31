N = int(input())
A = list(map(int,input().split()))
for i in range(1,N): A[i] += A[i-1]

M = int(input())
for _ in range(M):
    i,j = map(int, input().split())
    d = {0:-1}
    ans = 0
    for inx in range(i-1,j):
        if A[inx] in d: ans = max(ans, inx-d[A[inx]])
        else: d[A[inx]] = inx
    print(ans)