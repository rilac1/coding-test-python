import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
arr = [0]+[int(input()) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M+K)]
tree = [0]*(4*N)

def init(start, end, node):
    if start==end: 
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1)
    return tree[node]

def t_sum(start, end, node):
    global left, right
    if start>right or end<left: return 0
    if start>=left and end<=right: return tree[node]
    mid = (start+end)//2
    return t_sum(start,mid,node*2) + t_sum(mid+1,end,node*2+1)

def update(start, end, node):
    global index, diff
    if start<=index<=end:
        tree[node] += diff
        if start!=end:
            mid = (start+end)//2
            update(start,mid,node*2)
            update(mid+1,end,node*2+1)

init(1,N,1)
for c in cmd:
    if c[0]==1:
        index, diff = c[1], c[2]-arr[c[1]]
        arr[index] = c[2]
        update(1,N,1)
    elif c[0]==2:
        left, right = c[1], c[2]
        print(t_sum(1,N,1))