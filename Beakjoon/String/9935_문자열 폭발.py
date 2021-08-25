# 문자열 폭발
str = input()
bomb = input()
len_bomb = len(bomb)

stack = []
for i in str:
    stack.append(i)
    if i == bomb[-1] and "".join(stack[-len_bomb:]) == bomb:
        del stack[-len_bomb:]

if stack:
    print("".join(stack))
else:
    print('FRULA')
