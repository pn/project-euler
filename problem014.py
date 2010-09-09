#!/usr/bin/env python3
limit = 1000000

# solution 1
result = (1, 1)
for i in range(2, limit):
	n = i
	l = 1
	while n > 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n + 1
		l += 1
	if result[1] < l:
		result = (i, l)
	#print("%d: %d" % (i, l))
print(result[0])
