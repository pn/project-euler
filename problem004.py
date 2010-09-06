#!/usr/bin/env python
import sys

# solution 1
def is_palindrome(n):
	if len(n) != 6:
		return False	
	if n == n[::-1]:
		return True
	return False
m = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		prod = i*j
		if is_palindrome(str(prod)) and prod > m:
			m = i*j
print m
