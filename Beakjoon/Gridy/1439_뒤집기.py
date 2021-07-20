# 뒤집기
str = input()
num=[]
for i in str:
    num.append(int(i))

to0 = 0
to1 = 0
temp = num[0]
if temp == 1:
	to0 = 1
else:
	to1 = 1

for n in num[1:]:
	if temp != n:
		if n == 1:
			to0 += 1
		else:
			to1 += 1
	temp = n
print(min(to0, to1))