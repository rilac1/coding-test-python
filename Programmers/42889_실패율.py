# 실패율
import operator
def solution(N, stages):
    answer = []
    fail = {}
    for i in range(1,N+1):
        fail[i] = 0

    a = len(stages)
    for i in range(1,N+1):
        b = a 
        for s in stages:
            if i==s:
                fail[i] += 1
        a -= fail[i]
        if b==0:
            fail[i] == 0
        else:
            fail[i] /= b
    fail = sorted(fail.items(), key=lambda x: x[1], reverse=True)
    for i in fail:
        answer.append(i[0])
    return answer