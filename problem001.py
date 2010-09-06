#!/usr/bin/env python
limit = 1000

# solution 1
sum = 0
for i in range(limit):
	if not i % 3 or not i % 5:
		sum += i
print sum

# solution 2
def find_sum(i, limit):
	num = (limit-1)//i
	return (i + num*i) * num / 2

print find_sum(3, limit) + find_sum(5, limit) - find_sum(3*5, limit)
