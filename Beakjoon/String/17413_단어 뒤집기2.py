# 단어 뒤집기 2
str = input()
i = 0
while i<len(str):
    if str[i]=='<':
        while str[i]!='>':
            print(str[i],end='')
            i += 1
        print(str[i],end='')
        i += 1
    elif str[i]==' ':
        print(end=' ')
        i += 1
    else:
        s = []
        while i<len(str) and str[i]!='<' and str[i]!=' ':
            s.append(str[i])
            i += 1
        while s: print(s.pop(),end='')