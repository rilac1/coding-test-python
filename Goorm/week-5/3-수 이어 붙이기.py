from itertools import permutations

N = int(input())
cards = input().split()

ans = 1e18

for case in permutations(cards, N):
    result = case[0]
    for num in case[1:]:
        if result[-1] == num[0]:
            result += num[1:]
        else:
            result += num

    ans = min(ans, int(result))

print(ans)
