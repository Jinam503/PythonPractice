import random

b = []
while len(b) < 6:
	num = random.randint(1,45)
	if num not in b:
		b.append(num)
	
print(sorted(b))