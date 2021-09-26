# 괄호의 값
bracket = input()
stack = []
def recur():
    if str(stack[-1]).isdigit():
        return stack.pop()+recur()
    return 0

try:
    for b in bracket:
        if b==')':
            temp = max(recur(),1)
            if stack.pop() == '[': raise
            stack.append(2*temp)
        elif b==']':
            temp = max(recur(),1)
            if stack.pop() == '(': raise
            stack.append(3*temp)
        else: stack.append(b)
    print(sum(stack))
except: 
    print(0)