# 게리맨더링
N = int(input())
population = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i] = list(map(int, input().split()))[1:]

def search(left,num):
    if num <= (N>>1):
        checkDiff(picked)

    for i in range(left, N+1):
        picked[i] = True
        search(i+1, num+1)
        picked[i] = False

def checkDiff(bitMap):
    global ans
    a,b = [], []        # area
    ap,bp = 0,0         # population

    for i in range(1, N+1):
        if bitMap[i]:
            a.append(i)
            ap += population[i]
        else:
            b.append(i)
            bp += population[i]

    if isValid(a) and isValid(b):
        ans = min(ans, abs(ap - bp))

def isValid(area):
    if len(area)==0 or len(area)==N:
        return False
    checkDict = {}
    for city in area: checkDict[city] = True
    dfs(checkDict, area[0])
    return not checkDict

def dfs(check, node):
    del(check[node])
    for n in graph[node]:
        if n in check: dfs(check, n)

picked = [False] * (N+1)
ans = 1e9

search(1,0)
if ans==1e9: ans = -1
print(ans)