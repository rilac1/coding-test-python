t = int(input())

for _ in range(t):
    n = int(input())
    scores = list(map(int, input().split()))

    ans = 0
    avr = sum(scores) / n
    for score in scores:
        ans += int(score >= avr)

    print(str(ans) + '/' + str(n))
