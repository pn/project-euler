#!/usr/bin/env python3
edge = 20

# solution 1
sum = 0
for i in range(edge):
	sum += 2**(i)
sum *= -2
sum += 2**(edge+edge) - edge * 2
print(sum)
