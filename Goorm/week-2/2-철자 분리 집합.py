N = int(input())
s = input()

ans = 1
before = s[0]
for i in range(1, len(s)):
    if s[i] != before:
        before = s[i]
        ans += 1
print(ans)