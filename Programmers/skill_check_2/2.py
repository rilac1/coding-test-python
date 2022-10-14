import math

def solution(progresses, speeds):
    answer = []
    required_days = []

    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress
        required_days.append(math.ceil(remain/speed))

    count = 1
    day = required_days[0]
    for required_day in required_days[1:]:
        if required_day > day:
            answer.append(count)
            count = 1
            day = required_day
        else:
            count += 1
    answer.append(count)

    return answer
