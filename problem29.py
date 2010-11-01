#!/usr/bin/env python
limit = 100

t = []
for x in range(2, limit+1):
	for y in range(2, limit+1):
		t.append(x**y)
print(len(set(t)))
