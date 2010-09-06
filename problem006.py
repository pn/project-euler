#!/usr/bin/env python
limit = 100

# solution 1
sum = 0
for i in range(1, limit + 1):
	sum += i**2
print ((1 + limit)*limit/2)**2 - sum
