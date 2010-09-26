#!/usr/bin/env python3
num = 10000

# solution 1
divisors = [[1] for i in range(1, num+1)]
for i in range(2, num):
	k = 2*i
	while k < num:
		divisors[k].append(i)
		k += i
d = {}
for i in range(1, num):
	d[i] = sum(divisors[i])

result = 0
for i in d:
	if 1 < d[i] < num and d[i] != i and i == d[d[i]]:
		result += d[i] + d[d[i]]
		d[i] = 0
print(result)
