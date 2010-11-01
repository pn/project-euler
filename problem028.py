#!/usr/bin/env python
limit = 1001

last = s = 1
for n in range(3, limit + 1, 2):
	m = n - 1
	s += 3*last + m*6
	last = last + m*4
	s += last
print s
