import itertools
def solution(users, emoticons):
    answer = [0,0]
    rate_range = [10,20,30,40]
    rates = itertools.product(rate_range, repeat=len(emoticons))

    for rate in rates:
        plus_service = 0
        cost = 0

        discounted_emoticons = []
        for rate_per_emoticon, emoticon in zip(rate, emoticons):
            discounted_emoticons.append(emoticon * (100-rate_per_emoticon) // 100)

        for user in users:
            user_rate, max_money = user
            use_money = 0
            for i in range(len(emoticons)):
                if rate[i] >= user_rate:
                    use_money += discounted_emoticons[i]
            if use_money >= max_money:
                plus_service += 1
            else:
                cost += use_money

        if answer[0] < plus_service:
            answer[0] = plus_service
            answer[1] = cost
        elif answer[0] == plus_service:
            answer[1] = max(answer[1], cost)

    return answer

