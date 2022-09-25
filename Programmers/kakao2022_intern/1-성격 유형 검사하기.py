def solution(survey, choices):
    answer = ''
    types = 'RTCFJMAN'
    score = {s:0 for s in types}

    for survey_type, choice in zip(survey, choices):
        left = survey_type[0]
        right = survey_type[1]

        if choice == 1:
            score[left] += 3
        elif choice == 2:
            score[left] += 2
        elif choice == 3:
            score[left] += 1
        elif choice == 5:
            score[right] += 1
        elif choice == 6:
            score[right] += 2
        elif choice == 7:
            score[right] += 3

    answer += 'R' if score['R'] >= score['T'] else 'T'
    answer += 'C' if score['C'] >= score['F'] else 'F'
    answer += 'J' if score['J'] >= score['M'] else 'M'
    answer += 'A' if score['A'] >= score['N'] else 'N'
    return answer