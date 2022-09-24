def solution(today, terms, privacies):
    answer = []

    term_dict = {}
    for term in terms:
        term_type, month = term.split()
        term_dict[term_type] = int(month)

    for i in range(len(privacies)):
        time, term = privacies[i].split()
        date = add_month(time, term_dict[term])
        if is_expired(today, date):
            answer.append(i+1)

    return answer

def is_expired(today, date):
    return today >= date

def add_month(date, add_month):
    year, month, day = map(int, date.split("."))
    month += int(add_month)

    year += (month-1)//12
    month = (month-1) % 12 + 1

    year = str(year)
    month = str(month) if month >= 10 else '0'+str(month)
    day = str(day) if day >= 10 else '0'+str(day)

    return year + '.' + month + '.' + day
