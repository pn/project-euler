#!/usr/bin/env python
power = 1000

# solution 1
num = 2**power
s = 0
while num > 0:
	s += num % 10
	num = num // 10
print(s)
