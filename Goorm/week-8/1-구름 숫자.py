N = int(input())
goorm_number = input()

goorm_dict = {'qw': '1',
              'as': '2',
              'zx': '3',
              'we': '4',
              'sd': '5',
              'xc': '6',
              'er': '7',
              'df': '8',
              'cv': '9',
              'ze': '0'}

ans = goorm_dict[goorm_number[:2]]
for i in range(1, N-1):
    if goorm_number[i:i+2] in goorm_dict:
        ans += goorm_dict[goorm_number[i:i+2]]
print(ans)
