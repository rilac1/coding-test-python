# isharP
import copy
line = input().split()

for parts in line[1:]:
    type = copy.deepcopy(line[0])
    name = ''
    for i in parts:
        if i == ',' or i==';':
            continue
        elif 'A'<= i <='Z' or 'a'<= i <='z':
            name = name+i
        else:
            type = type + i
    print(type, name+';')