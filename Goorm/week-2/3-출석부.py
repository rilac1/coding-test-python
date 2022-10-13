import sys
input = sys.stdin.readline

N, k = map(int, input().split())
people = [input().split() for _ in range(N)]
people.sort()
print(*people[k-1])
