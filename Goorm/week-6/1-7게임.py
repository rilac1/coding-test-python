even = [0, 2, 4, 6]
odd = [1, 3, 5]

for _ in range(5):
    result = 0
    K = input()
    for num in even:
        result += int(K[num])
    for num in odd:
        if K[num] != '0':
            result *= int(K[num])

    print(result % 10)
