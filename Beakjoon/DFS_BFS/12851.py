# 숨바꼭질 2
from collections import deque
N, K = map(int, input().split())

min_path = [-1] * 100001
path_num = [0] * 100001
min_path[N] = 0
path_num[N] = 1

queue = deque([N])
while queue:
    x = queue.popleft()
    for i in (x+1, x-1, x*2):
        if 0<=i<100001:
            if min_path[i]==-1:
                min_path[i] = min_path[x]+1
                path_num[i] = path_num[x]
                queue.append(i)
            elif min_path[i] == min_path[x]+1:
                path_num[i] += path_num[x]

print(min_path[K])
print(path_num[K])