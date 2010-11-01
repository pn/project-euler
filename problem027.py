#!/usr/bin/env python
limit = 1000

def is_prime(n):
	if n < 2:
		return False
	for d in range(2, int(n**0.5)+1):
		if n % d == 0:
			return False
	return True

def f(a, b):
	return lambda n: (n+a)*n+b

maximum = 0
max_a, max_b = 0, 0
for b in range(-limit+1, limit):
	if not is_prime(abs(b)):
		continue
	for a in range(-limit+1, limit):
		funct = f(a, b)
		n = 0
		while is_prime(funct(n)):
			n += 1
			if n - 1 > maximum:
				max_a, max_b = a, b
				maximum = n - 1

print(max_a*max_b)
