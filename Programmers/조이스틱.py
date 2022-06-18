from copy import deepcopy
from itertools import product

def solution(name):
    move_count = []
    mask = [False]*len(name)
    for i, n in enumerate(name):
        if n=='A': mask[i] = True

    for order in product((-1,1), repeat=len(name)-1):
        order = list(order)
        m = deepcopy(mask)
        i=0
        try:
            while (False in m):
                i += order.pop()
                m[i] = True
        except: continue
        move_count.append(len(name)-len(order))

    return min(move_count)-1 + sum([min(ord(a)-ord('A'), ord('Z')-ord(a)+1) for a in name])
