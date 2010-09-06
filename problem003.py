#!/usr/bin/env python3
import math
number = 600851475143

# solution 1
def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True
limit = int(math.sqrt(number))
for i in range(limit, 2, -1):
	if is_prime(i) and not number % i:
		print(i)
		break
