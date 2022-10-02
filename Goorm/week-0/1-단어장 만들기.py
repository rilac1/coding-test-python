import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
words.sort(key=lambda x: (len(x), x))
print(words)
