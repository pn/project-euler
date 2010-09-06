#!/usr/bin/env python
import sys
limit = 1000
num = 500

# solution 1 (brute force...)
for a in range(1, num+1):
	for b in range(1, num+1):
		for c in range(1, num+1):
			if a < b < c and a**2 + b**2 == c**2 and a + b + c == limit:
				print(a*b*c)
				sys.exit(0)
	
