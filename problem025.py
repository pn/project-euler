#!/usr/bin/env python
limit = (10**1000-1)/10

# solution 1
i, a, b = 1, 1, 1
while a <= limit:
	a, b = b, a + b
	i += 1
print i
