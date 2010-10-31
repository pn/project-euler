#!/usr/bin/env python3
import sys
num_divisors = 500

# solution 1
def triangle(n):
	return (1+n)*n/2

def is_prime(n):
	for d in range(2, int(n**0.5)+1):
		if n % d == 0:
			return False
	return True

def get_primes(n):
	t, p = [2], 3
	for i in range(n):
		while not is_prime(p):
			p += 2
		t.append(p)
		p += 2
	return t

primes = get_primes(num_divisors*10)

def prime_factors(n):
	pf = {}
	for p in primes:
		while n % p == 0:
			pf[p] = pf.get(p, 0) + 1
			n = n / p
		if n == 1:
			break;
	return pf

def num_divs(n):
	divs = 1
	pf = prime_factors(n)
	for p in pf:
		divs *= pf[p] + 1
	return divs
n = 1
divs = 1
m_divs = 1
while divs <= num_divisors:
	n += 1
	t = triangle(n)
	divs = num_divs(t)
	if divs > m_divs:
		m_divs = divs
print(int(triangle(n)))
