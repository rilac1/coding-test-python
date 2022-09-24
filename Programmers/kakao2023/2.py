from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery_q = deque()
    pickup_q = deque()

    for i in range(n):
        if deliveries[i] > 0:
            delivery_q.appendleft((i,deliveries[i]))
        if pickups[i] > 0:
            pickup_q.appendleft((i,pickups[i]))

    while delivery_q or pickup_q:
        if delivery_q and pickup_q:
            destination = max(delivery_q[0][0], pickup_q[0][0])
        elif delivery_q:
            destination = delivery_q[0][0]
        else:
            destination = pickup_q[0][0]

        load_or_pickup(delivery_q, cap)
        load_or_pickup(pickup_q, cap)

        answer += (destination+1)*2

    return answer

def load_or_pickup(q, cap):
    in_truck = 0
    while in_truck <= cap:
        if not q:
            break
        next_load = q.popleft()
        next_visit = next_load[0]
        in_truck += next_load[1]
    if in_truck > cap:
        q.appendleft((next_visit, in_truck - cap))
