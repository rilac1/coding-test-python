from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    for i in range(len(q1)*4):
        if sum_q1 == sum_q2:
            return i
        elif sum_q1 > sum_q2:
            val = q1.popleft()
            sum_q1 -= val
            sum_q2 += val
            q2.append(val)
        else:
            val = q2.popleft()
            sum_q1 += val
            sum_q2 -= val
            q1.append(val)

    return -1