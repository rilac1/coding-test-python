import math

def solution(fees, records):
    answer = []
    parking_lot = {}
    car_time = {}

    for record in records:
        record = record.split()
        time = record[0]
        car = record[1]
        if car in parking_lot:
            using_time = cal_time(parking_lot[car], time)
            del parking_lot[car]

            if car in car_time:
                car_time[car] += using_time
            else:
                car_time[car] = using_time
        else:
            parking_lot[car] = time

    for car in parking_lot.keys():
        using_time = cal_time(parking_lot[car], "23:59")
        if car in car_time:
            car_time[car] += using_time
        else:
            car_time[car] = using_time

    for car in sorted(car_time.keys()):
        time = car_time[car]
        answer.append(cal_rate(fees, time))

    return answer


def cal_time(in_time, out_time):
    in_time = tuple(map(int, in_time.split(':')))
    out_time = tuple(map(int, out_time.split(':')))

    return (out_time[0] - in_time[0]) * 60 + (out_time[1] - in_time[1])


def cal_rate(fees, time):
    base_time = fees[0]
    base_rate = fees[1]
    unit_time = fees[2]
    unit_rate = fees[3]
    upper_time = time - base_time

    return base_rate + unit_rate * max(0, math.ceil(upper_time / unit_time))


fee = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fee, records))
