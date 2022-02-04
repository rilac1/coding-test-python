arr  = [1,2,3,4]

picked = []
def comb(n, r, left):
    if len(picked) == r:
        print(picked)
        return

    for i in range(left, n):        # left ~ n까지만 탐색
        picked.append(arr[i])       # 변화
        comb(n, r, i+1)             # 재귀호출 (마지막에 넣었던 index가 left가 된다.)
        picked.pop()  
comb(4,2,0)