def solution(id_list, reports, k):
    answer = [0] * len(id_list)

    id_dict = {id_:i for i, id_ in enumerate(id_list)}
    report_histories = {id_:set() for id_ in id_list}

    for report in reports:
        reporting, reported = report.split()
        report_histories[reported].add(reporting)

    for report_history in report_histories.items():
        id_, reporters = report_history
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_dict[reporter]] += 1

    return answer
