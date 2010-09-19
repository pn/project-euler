#!/usr/bin/env python
num = 100

result = 1
for i in range(1, num+1):
	result *= i
print sum([int(s) for s in str(result)])
