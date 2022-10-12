n = int(input())
A = [0] + list(map(int, input().split()))

def get_prime(n):
    prime_mask = [True] * (n+1)

    for i in range(2, int(n**0.5)+1):
        if not prime_mask[i]:
            continue
        num = i * 2
        while num <= n:
            prime_mask[num] = False
            num += i

    prime = []
    for i in range(2, n+1):
        if prime_mask[i]:
            prime.append(i)

    return prime

ans = 0
for prime_num in get_prime(n):
    ans += A[prime_num]
print(ans)

# Better Code
"""
def get_prime(n):
    check = [True] * (n + 1)

    for i in range(2, int(n ** .5) + 1):
        if not check[i]:
            continue
        for j in range(i + i, n + 1, i):
            check[j] = False
    
    return [i for i in range(2, n + 1) if check[i]]
"""
