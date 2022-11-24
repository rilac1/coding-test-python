import string

N = int(input())
S = input()

ans = ''
alphabets = list(string.ascii_lowercase)
for i in range(0,N,2):
    index = (ord(S[i]) - ord('a') + (int(S[i+1])**2)) % 26
    ans += alphabets[index]
print(ans)
