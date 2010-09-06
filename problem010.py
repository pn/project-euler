#!/usr/bin/env python
import sys
limit = 2000000

# solution 1
def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True
sum = 0
for i in range(2, limit):
	if is_prime(i):
		sum+=i
print sum
