def make_phone():
    phone = [[] for _ in range(10)]
    phone[1] = ['1','.', ',', '?', '!']

    alpha = ord('A')
    for i in range(2, 10):
        phone[i].append(str(i))

        default = 3
        if i == 7 or i == 9:
            default += 1
        for _ in range(default):
            phone[i].append(chr(alpha))
            alpha += 1

    return phone


def push_button(button, index):
    length = len(phone[int(button)])
    return phone[int(button)][index % length]


n = int(input())
s = input()

phone = make_phone()
last_button = s[0]
index = 0
answer = ''

for button in s[1:]:
    if button == last_button:
        index += 1
    else:
        answer += push_button(last_button, index)
        last_button = button
        index = 0
answer += push_button(last_button, index)

print(answer)