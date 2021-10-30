# 잃어버린 괄호
a = input().split('-')
for i in range(len(a)):
    try: t = sum(map(int, a[i].split('+')))
    except: t = int(a[i])
    if i==0: x=t
    else: x-=t
print(x)