#!/usr/bin/env python
limit = 4000000

# solution 1
a, b = 0, 1
sum = 0
while b < limit:
	if not b % 2:
		sum += b
	a, b = b, a + b
print sum
