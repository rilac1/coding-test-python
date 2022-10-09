input()
ans = 1
for bridge in map(int, input().split()):
    ans *= bridge
print(ans)
