def solution(land):
    for row in range(1, len(land)):
        for col in range(4):
            temp = land[row-1][col]

            land[row-1][col] = 0
            land[row][col] += max(land[row-1])
            land[row-1][col] = temp

    return max(land[-1])
