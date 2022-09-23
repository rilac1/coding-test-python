def solution(id_list, reports, k):
    answer = []
    mail_users = {user: 0 for user in id_list}
    report_count = {user: 0 for user in id_list}
    report_users = {user: set() for user in id_list}

    for report in reports:
        a, b = report.split()
        if a not in report_users[b]:
            report_count[b] += 1
            report_users[b].add(a)

    for user in id_list:
        if report_count[user] >= k:
            for mail_user in report_users[user]:
                mail_users[mail_user] += 1

    for user in id_list:
        answer.append(mail_users[user])

    return answer
