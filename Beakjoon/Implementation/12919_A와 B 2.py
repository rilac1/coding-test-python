S, T = input(), input()

def dfs(t):
    if len(t) == len(S):
        if t == S:
            print(1)
            exit(0)
        return
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])
dfs(T)
print(0)
