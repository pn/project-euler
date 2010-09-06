#!/usr/bin/env python
limit = 10001

# solution 1
def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True
num = 2
for i in range(1, limit+1):
	while not is_prime(num):
		num+=1
	if i == limit:
		break
	num+=1
print(num)
