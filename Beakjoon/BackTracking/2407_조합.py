# 조합
N, M = map(int, input().split())
if N-M<M:  M=N-M
def recur(N,M):
    if M==0: return 1
    return N*recur(N-1, M-1)
print(recur(N,M)//recur(M,M))