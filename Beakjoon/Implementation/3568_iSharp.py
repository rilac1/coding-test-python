# iSharp
import copy
line = input().split()

for parts in line[1:]:
    type = copy.deepcopy(line[0])
    name = ''
    for i in parts[::-1]:
        if i == ',' or i==';':
            continue
        elif 'A'<= i <='Z' or 'a'<= i <='z':
            name = name+i
        elif i == '[':
            type = type + ']'
        elif i == ']':
            type = type + '['
        else:
            type = type + i
    print(type, name[::-1]+';')