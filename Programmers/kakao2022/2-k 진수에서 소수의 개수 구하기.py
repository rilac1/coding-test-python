def solution(n, k):
    remainders = get_remainders(k, n)
    condition_numbers = list(filter(None, remainders.split('0')))

    answer = 0
    for condition_number in condition_numbers:
        if is_prime(int(condition_number)):
            answer += 1

    return answer

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def get_remainders(k, n):
    remainders = []
    while n:
        remainders.append(n % k)
        n //= k
    return "".join(map(str, remainders[::-1]))
