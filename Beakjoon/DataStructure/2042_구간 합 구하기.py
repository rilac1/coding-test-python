# 구간 합 구하기
## 세그먼트 트리
import sys
input = sys.stdin.readline
N,M,K = map(int, input().split())

tree = [0]*(4*N)
index = []
def init(start, end, node):
    if start==end:
        tree[node] = int(input())
        index.append(node)
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2) + \
        init(mid+1,end,node*2+1)
    return tree[node]
init(0,N-1,1)

def t_sum(start, end, node):
    global left, right
    if start>right or end<left: return 0
    if start>=left and end<=right: return tree[node]
    mid = (start+end)//2
    return t_sum(start,mid,node*2) +\
         t_sum(mid+1,end,node*2+1)

def update(start, end, node):
    global target, diff
    if start>target or end<target: return
    tree[node] += diff
    if start==end: return;
    mid = (start+end)//2
    update(start,mid,node*2)
    update(mid+1,end,node*2+1)

cmd = [list(map(int, input().split())) for _ in range(M+K)]
for c in cmd:
    if c[0]==1:
        target, diff = c[1]-1, c[2]-tree[index[c[1]-1]]
        update(0,N-1,1)
    elif c[0]==2:
        left, right = c[1]-1, c[2]-1
        print(t_sum(0,N-1,1))