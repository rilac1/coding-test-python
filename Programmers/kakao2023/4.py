def solution(numbers):
    answer = []

    return answer

def to_binary(number):
    answer = ''
    while number > 1:
        answer += str(number % 2)
        number //= 2
    answer += str(number)
    return answer[::-1]

print(to_binary(95))