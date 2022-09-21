def solution(p):
    return recursion(p)


def recursion(p):
    # 1
    if not p or is_proper(p):
        return p

    # 2
    u, v = tear(p)

    # 3
    if is_proper(u):
        return u + recursion(v)

    # 4-1 ~ 4.3
    temp = '(' + recursion(v) + ')'

    # 4-4 ~ 4-5
    return temp + preprocess(u)


def tear(p):
    start = p[0]
    stack = [start]

    i = 1
    while stack:
        if p[i] == start:
            stack.append(p[i])
        else:
            stack.pop()
        i += 1

    return p[:i], p[i:]


def is_proper(p):
    stack = []

    for bracket in p:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def preprocess(u):
    u = list(u[1:-1])

    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('

    return "".join(u)
