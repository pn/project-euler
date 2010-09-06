#!/usr/bin/env python

# solution 1
def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)
def lcm(r):
	if len(r) == 1:
		return r[:1]
	if len(r) == 2:
		return [r[0] * r[1] / gcd(r[0], r[1])]
	else:
		return lcm(r[:1] + lcm(r[1:]))
print(lcm(range(1, 21))[0])
