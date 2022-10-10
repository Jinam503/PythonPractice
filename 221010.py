members = ['백진암', '김준경', '이희승', '마현우']
i = 0
while i < len(members):
    print(members[i])
    i = i + 1
print(f'{members.pop()} ㅂㅇㅋㅋ')
print(members)
members.remove('김준경')
print(members)
members.insert(0, '정상수')
print(members)
print(members.index('이희승'))
members.insert(len(members), '신태일')
print(members)

print(list(reversed(members)))



for item in range(5, 11): #5부터 10까지
    print(item, end = ' ')
	
print()
for i in range(1,101):
	if i % 2 == 0 :
		print(i, end = ' ')


a = int(input("숫자를 입력하세요"))
i = 0
while i < a:
    print('Hello world')
    i = i + 1