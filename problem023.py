#!/usr/bin/env python3
from math import sqrt
limit = 28123

result = 0
abundant = set()
for x in range(1, limit):
	q = int(sqrt(x))
	s = 1+sum(y + x/y for y in range(2, q+1) if not x%y)
	if q*q == x: s -= q
	if s > x: abundant.add(x)
	if not any([((x-a) in abundant) for a in abundant]): result += x
print(result)
