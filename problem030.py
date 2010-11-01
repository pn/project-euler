#!/usr/bin/env python
limit = 1000

def checkNumber(n):
	s = 0
	for c in str(n):
		s+=int(c)**5
	if s == n:
		return True
	return False

numbers = []

for i in range(2, 1000000):
	if checkNumber(i):
		numbers.append(i)
print(sum(numbers))
